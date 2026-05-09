<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import 'leaflet/dist/leaflet.css';
import * as L from 'leaflet';

const isConnected = ref(false);
const vehicles = ref<any[]>([]);
let map: L.Map | null = null;
let markers: { [key: string]: L.Marker } = {};
let fetchInterval: number | null = null;

// Fix dla ikon Leaflet w Vite
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

const fetchRealtimeData = async () => {
  try {
    const res = await fetch('http://localhost:8000/realtime');
    const data = await res.json();
    vehicles.value = data;
    isConnected.value = true;
    updateMap(data);
  } catch (e) {
    isConnected.value = false;
    console.error('Błąd pobierania danych z API', e);
  }
};

const updateMap = (data: any[]) => {
  if (!map) return;
  
  // Usuń stare markery których nie ma w nowych danych
  const newIds = new Set(data.map(v => v.vehicle_id || v.trip_id));
  Object.keys(markers).forEach(id => {
    if (!newIds.has(id)) {
      map!.removeLayer(markers[id]);
      delete markers[id];
    }
  });

  // Dodaj/odśwież markery
  data.forEach(vehicle => {
    if (!vehicle.latitude || !vehicle.longitude) return;
    const vId = vehicle.vehicle_id || vehicle.trip_id;
    if (markers[vId]) {
      markers[vId].setLatLng([vehicle.latitude, vehicle.longitude]);
      markers[vId].setPopupContent(`Trasa/Przejazd: ${vehicle.trip_id || ''}<br>Pojazd: ${vehicle.vehicle_id || 'Nieznany'}`);
    } else {
      const marker = L.marker([vehicle.latitude, vehicle.longitude]).bindPopup(
        `Trasa/Przejazd: ${vehicle.trip_id || ''}<br>Pojazd: ${vehicle.vehicle_id || 'Nieznany'}`
      );
      marker.addTo(map!);
      markers[vId] = marker;
    }
  });

  // Ustaw widok na pierwsze auto jeśli jeszcze nie zmieniano
  if (data.length > 0 && map.getZoom() === 6) {
    map.setView([data[0].latitude, data[0].longitude], 12);
  }
};

onMounted(() => {
  // Inicjalizacja pliku z mapą z widokiem na Polskę
  map = L.map('map').setView([52.069, 19.48], 6);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  fetchRealtimeData();
  fetchInterval = setInterval(fetchRealtimeData, 5000) as unknown as number;
});

onUnmounted(() => {
  if (fetchInterval) clearInterval(fetchInterval);
  if (map) map.remove();
});
</script>

<template>
  <main class="min-h-screen bg-slate-900 p-8 w-full mx-auto flex flex-col gap-6 text-slate-100 font-sans">
    <header class="flex justify-between items-center bg-slate-800 p-6 rounded-xl border border-slate-700">
      <div>
        <h1 class="text-3xl font-bold tracking-tight mb-1">T:H:RUST GPS</h1>
        <p class="text-slate-400 text-sm font-medium uppercase">Live Map Dashboard</p>
      </div>
      <div class="flex items-center gap-4">
        <span>Aktywne pojazdy: <strong class="text-white">{{ vehicles.length }}</strong></span>
        <span :class="isConnected ? 'text-green-400' : 'text-red-500'">
          {{ isConnected ? 'API CONNECTED' : 'DISCONNECTED' }}
        </span>
      </div>
    </header>

    <div class="w-full bg-slate-800 rounded-xl p-4 h-[70vh]">
      <div id="map" class="w-full h-full rounded-lg"></div>
    </div>

  </main>
</template>
