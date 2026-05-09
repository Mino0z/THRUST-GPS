import asyncio
import pandas as pd
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import json
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="T/H/RUST GPS Live Telemetry API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TelemetryData(BaseModel):
    feature_1: float = Field(default=0.0)
    feature_2: float = Field(default=0.0)
    feature_3: float = Field(default=0.0)
    feature_4: float = Field(default=0.0)
    feature_5: float = Field(default=0.0)
    feature_6: float = Field(default=0.0)
    feature_7: float = Field(default=0.0)
    feature_8: float = Field(default=0.0)
    feature_9: float = Field(default=0.0)
    feature_10: float = Field(default=0.0)
    feature_11: float = Field(default=0.0)
    feature_12: float = Field(default=0.0)
    feature_13: float = Field(default=0.0)
    trust_index: float = Field(description="Calculated trust index from 0 to 100%")
    label: str = Field(description="Spoofing label")

@app.websocket("/api/flight-stream")
async def flight_stream(websocket: WebSocket):
    await websocket.accept()
    logger.info("WebSocket connected")
    
    try:
        try:
            # Replace with the actual path to your CSV file
            df = pd.read_csv("gps_data.csv")
        except FileNotFoundError:
            # Fallback mock data if file doesn't exist yet
            logger.warning("gps_data.csv not found, using dummy data.")
            df = pd.DataFrame([
                {**{f"feature_{i}": i * 0.1 for i in range(1, 14)}, "label": "authentic"},
                {**{f"feature_{i}": i * 0.5 for i in range(1, 14)}, "label": "simplistic"},
                {**{f"feature_{i}": i * 1.0 for i in range(1, 14)}, "label": "sophisticated"}
            ])
            
        for _, row in df.iterrows():
            label = str(row.get("label", "authentic")).lower()
            
            # Trust logic mapping based on label
            trust_index = 100.0
            if "simplistic" in label:
                trust_index = 30.0
            elif "intermediate" in label:
                trust_index = 15.0
            elif "sophisticated" in label:
                trust_index = 5.0
            elif "authentic" not in label:
                trust_index = 0.0

            # Safe extraction of 13 features
            features = []
            for i in range(13):
                # Adjust column reading if your CSV has named headers like 'f1', 'feature_1' etc.
                val = row.iloc[i] if i < len(row.index) else 0.0
                try:
                    features.append(float(val))
                except (ValueError, TypeError):
                    features.append(0.0)
            
            data = TelemetryData(
                feature_1=features[0], feature_2=features[1], feature_3=features[2],
                feature_4=features[3], feature_5=features[4], feature_6=features[5],
                feature_7=features[6], feature_8=features[7], feature_9=features[8],
                feature_10=features[9], feature_11=features[10], feature_12=features[11],
                feature_13=features[12],
                trust_index=trust_index,
                label=row.get("label", "authentic")
            )
            
            await websocket.send_json(data.model_dump())
            await asyncio.sleep(1) # stream rows 1 by 1 every second
            
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception as e:
        logger.error(f"Error streaming data: {e}")
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

