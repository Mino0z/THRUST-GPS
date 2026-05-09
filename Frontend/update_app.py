import sys
code = """<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
interface TelemetryData {
  feature_1: number; feature_2: number; feature_3: number;
  feature_4: number; feature_5: number; feature_6: number;
  feature_7: number; feature_8: number; feature_9: number;
  feature_10: number; feature_11: number; feature_12: number;
  feature_13: number;
  trust_index: number;
  label: string;
}
const isConnected = ref(false);
const latestTelemetry = ref<TelemetryData | null>(null);
let ws: WebSocket | null = null;
const connectWebSocket = () => {
  ws = new WebSocket('ws://localhost:8000/api/flight-stream');
  ws.onopen = () => { isConnected.value = true; };
  ws.onmessage = (event) => {
    try {
      latestTelemetry.value = JSON.parse(event.data);
    } catch(e) {}
  };
  ws.onclose = () => {
    isConnected.value = false;
    setTimeout(connectWebSocket, 3000);
  };
};
onMounted(() => connectWebSocket());
onUnmounted(() => { if (ws) ws.close(); });
</script>
<template>
  <main class="min-h-screen bg-slate-900 p-8 w-full max-w-7xl mx-auto flex flex-col gap-6 text-slate-100 font-sans">
    <header class="flex justify-between items-center bg-slate-800 p-6 rounded-xl border border-slate-700">
      <div>
        <h1 class="text-3xl font-bold tracking-tight mb-1 flex items-center gap-3">
          T/H/RUST GPS
          <span class="text-xs font-mono bg-violet-900/50 text-violet-300 border border-violet-500 rounded px-2 py-0.5">DEVlet ws: WebSocket | null = null;
const connectWebSocket-4const connectWebSocket = () => e"  ws = new WebSocket('ws://loca D  ws.onopen = () => { isCo      <div class="flex items-center g  ws.onmessage = (event) => {
    try {
      lat"     try {
      latestTelemegr      la :    } catch(e) {}
  };
  ws.onclose = () => {
    isEE  };
 VE' : 'CONNE  wON    isConn        </spa           <div class="w-3 h-3   };
};
onMounted(() => connectWebSockCo};
ctod onUnmounted(() => { if (ws) ws.closdi</script>
<templ    </header>
    <div v-if=<templatel  <main cla    <header class="flex justify-between items-center bg-slate-800 p-6 rounded-xl border border-slate-700">
      <dou      <div>
        <h1 class="text-3xl font-bold tracking-tight mb-1 flex items-center gap-3">
         ss        <hle          T/H/RUST GPS
          <span class="text-xs font-mono bg-violet-900/50 t)]          <span classtrconst connectWebSocket-4const connectWebSocket = () => e"  ws = new WebSocket('ws://loca D  ws.onopen = () => { isCo      <div class="flex ite        <h2 cl    try {
      lat"     try {
      latestTelemegr      la :    } catch(e) {}
  };
  ws.onclose = () => {
    isEE  };
 VE' : 'CONNE  wON    isConn        </spa           <div clas80      la-g      latestTelemegTe  };
  ws.onclose = () => {
    isEE  };
 VE'  '  wt-    isEE  };          { VE' : 'CONem};
onMounted(() => connectWebSockCo};
ctod onUnmounted(() => {        </div>
   ctod onUnmounted(() => { 5 py-1.5 t<templ    </header>
    <div v-if=<templateder track    <div v-               <dou      <div>
        <h1 class="text-3xl font-bold tracking-tight mb-1 flex items-center gap-3">
         ss        <hle          Ted        <h1 class="t>
         ss        <hle          T/H/RUST GPS
          <span c      </section>
      <section class="col-span-1 md:col-span-8 bg-      lat"     try {
      latestTelemegr      la :    } catch(e) {}
  };
  ws.onclose = () => {
    isEE  };
 VE' : 'CONNE  wON    isConn        </spa           <div clas80      la-g      latestTelemegTe  };
  ws.onclose = () => {
    isEE  };
 VEg-      latestTelemeg</  };
         </h2>
        <div class="grid grid-col    isEE  };
 VE' : ':g VE' : 'CONga  ws.onclose = () => {
    isEE  };
 VE'  '  wt-    isEE  };          { VE' : 'CONem};
onMounted(r- late-700/50 flex flex-col gap-1 traonMounted(() => connectWebSockCo};
ctod onUnmount
            <span class="text-[10px]  ext-slate-500 uppercase tracking-wide    <div v-if=<templateder track    <div             <span        <h1 class="text-3xl font-bold tracking-tight mb-1 flex i                   ss        <hle          Ted        <h1 class="t>
         ss        <hle            ss                 </div>
        </div>
      </section>
    </div>
    <div v-else class="h-64 flex justify-center items-center bg-slate-800 rounded-xl border border-slate-700 shadow-inner">
         };
  ws.onclose = () => {
    isEE  };
 VE' -m  w t    isEE  };
 VE' : 'te VE' : 'CONap  ws.onclose = () => {
    isEE  };
 VEg-      latestTelemeg</  };
         </h2>
        <div cl f    isEE  };
 VEg-    0 VEg-      rc         </h2>
        <div c c        <div  s VE' : ':g VE' : 'CONga  ws.onclose = () => le    isEE  };
 VE'  '  wt-    isEE  };       "  VE'  '  wt8 onMounted(r- late-700/50 flex flex-col gap-1 trao.9ctod onUnmount
       1.135 5.824 3 7.938l3-2.647z"></path></svg>
         AWAITING DRONE TRANSMIS         ss        <hle            ss                 </div>
        </div>
      </section>
    </div>
    <div v-else class="h-64 flex justify-center items-center bg-slate-800 rounded-xl bordecat > write_vue.py << 'EOL'
import textwrap
code = """<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
interface TelemetryData {
  feature_1: number; feature_2: number; feature_3: number;
  feature_4: number; feature_5: number; feature_6: number;
  feature_7: number; feature_8: number; feature_9: number;
  feature_10: number; feature_11: number; feature_12: number;
  feature_13: number;
  trust_index: number;
  label: string;
}
const isConnected = ref(false);
const latestTelemetry = ref<TelemetryData | null>(null);
let ws: WebSocket | null = null;
const connectWebSocket = () => {
  ws = new WebSocket('ws://localhost:8000/api/flight-stream');
  ws.onopen = () => { isConnected.value = true; };
  ws.onmessage = (event) => {
    try {
      latestTelemetry.value = JSON.parse(event.data);
    } catch(e) {}
  };
  ws.onclose = () => {
    isConnected.value = false;
    setTimeout(connectWebSocket, 3000);
  };
};
onMounted(() => connectWebSocket());
onUnmounted(() => { if (ws) ws.close(); });
</script>
<template>
  <main class="min-h-screen bg-slate-900 p-8 w-full mx-auto flex flex-col gap-6 text-slate-100 font-sans">
    <header class="flex justify-between items-center bg-slate-800 p-6 rounded-xl border border-slate-700">
      <div>
        <h1 class="text-3xl font-bold tracking-tight mb-1">T/H/RUST GPS</h1>
        <p class="text-slate-400 text-sm font-medium uppercase">Live Telemetry Dashboard</p>
      </div>
      <div>
        <span :class="isConnected ? 'text-green-400' : 'text-red-500'">
          {{ isConnected ? 'CONNECTED' : 'DISCONNECTED' }}
        </span>
      </div>
    </header>
    <div v-if="latestTelemetry" class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <section class="bg-slate-800 rounded-xl p-6 flex flex-col items    } catc        <h2 class="text-xl mb-4">Trust Index  };
         <div  was    isConnected.value"     setTimeout(elemetry.trust_i  };
};
onMounted(() => connectWebSocked};
0'o>
          {{ latestTelemetry.trust_index.toFixed(1) }}%
        </div>
        <div class="mt-4 px-4 p    <header class="flex justify-between items-center bg-slate-800 p-6 rounded-xl border border-slate-700"0       <div>
        <h1 class="text-3xl font-bold tracking-tight mb-1">T/H/RUST GPS</h1>
        <        <                    <p class="text-slate-400 text-sm font-medium uppercase">Live Teleme>
      </div>
      <div>
        <span :class="isConnected ? 'text-green-400' : 'text-red-5ol      <div>-c        <s4"          {{ isConnected ? 'CONNECTED' : 'DISCONNECTED' }}
        </sde        </span>
      </div>
              <span class="text-xs text-slate-    </heade}}    <div v-i
       <section class="bg-slate-800 rounded-xl p-6 flex flex-col items    } ca_'         <div  was    isConnected.value"     setTimeout(elemetry.t        </div>
      </section>
    </div>
  </main>
</template>
"""
with open("src/App.vue", "w") as f:
    f.write(code)
EOL
python3 write_vue.py
echo -n "PHNjcmlwdCBzZXR1cCBsYW5nPSJ0cyI+CmltcG9ydCB7IHJlZiwgb25Nb3VudGVkLCBvblVubW91bnRlZCB9IGZyb20gJ3Z1ZSc7CgppbnRlcmZhY2UgVGVsZW1ldHJ5RGF0YSB7CiAgZmVhdHVyZV8xOiBudW1iZXI7IGZlYXR1cmVfMjogbnVtYmVyOyBmZWF0dXJlXzM6IG51bWJlcjsKICBmZWF0dXJlXzQ6IG51bWJlcjsgZmVhdHVyZV81OiBudW1iZXI7IGZlYXR1cmVfNjogbnVtYmVyOwogIGZlYXR1cmVfNzogbnVtYmVyOyBmZWF0dXJlXzg6IG51bWJlcjsgZmVhdHVyZV85OiBudW1iZXI7CiAgZmVhdHVyZV8xMDogbnVtYmVyOyBmZWF0dXJlXzExOiBudW1iZXI7IGZlYXR1cmVfMTI6IG51bWJlcjsKICBmZWF0dXJlXzEzOiBudW1iZXI7CiAgdHJ1c3RfaW5kZXg6IG51bWJlcjsKICBsYWJlbDogc3RyaW5nOwp9Cgpjb25zdCBpc0Nvbm5lY3RlZCA9IHJlZihmYWxzZSk7CmNvbnN0IGxhdGVzdFRlbGVtZXRyeSA9IHJlZjxUZWxlbWV0cnlEYXRhIHwgbnVsbD4obnVsbCk7CmxldCB3czogV2ViU29ja2V0IHwgbnVsbCA9IG51bGw7Cgpjb25zdCBjb25uZWN0V2ViU29ja2V0ID0gKCkgPT4gewogIHdzID0gbmV3IFdlYlNvY2tldCgnd3M6Ly9sb2NhbGhvc3Q6ODAwMC9hcGkvZmxpZ2h0LXN0cmVhbScpOwogIHdzLm9ub3BlbiA9ICgpID0+IHsgaXNDb25uZWN0ZWQudmFsdWUgPSB0cnVlOyB9OwogIHdzLm9ubWVzc2FnZSA9IChldmVudCkgPT4gewogICAgdHJ5IHsKICAgICAgbGF0ZXN0VGVsZW1ldHJ5LnZhbHVlID0gSlNPTi5wYXJzZShldmVudC5kYXRhKTsKICAgIH0gY2F0Y2goZSkge30KICB9OwogIHdzLm9uY2xvc2UgPSAoKSA9PiB7CiAgICBpc0Nvbm5lY3RlZC52YWx1ZSA9IGZhbHNlOwogICAgc2V0VGltZW91dChjb25uZWN0V2ViU29ja2V0LCAzMDAwKTsKICB9Owp9OwoKb25Nb3VudGVkKCgpID0+IGNvbm5lY3RXZWJTb2NrZXQoKSk7Cm9uVW5tb3VudGVkKCgpID0+IHsgaWYgKHdzKSB3cy5jbG9zZSgpOyB9KTsKPC9zY3JpcHQ+Cgo8dGVtcGxhdGU+CiAgPG1haW4gY2xhc3M9Im1pbi1oLXNjcmVlbiBiZy1zbGF0ZS05MDAgcC04IHctZnVsbCBteC1hdXRvIGZsZXggZmxleC1jb2wgZ2FwLTYgdGV4dC1zbGF0ZS0xMDAgZm9udC1zYW5zIj4KICAgIDxoZWFkZXIgY2xhc3M9ImZsZXgganVzdGlmeS1iZXR3ZWVuIGl0ZW1zLWNlbnRlciBiZy1zbGF0ZS04MDAgcC02IHJvdW5kZWQteGwgYm9yZGVyIGJvcmRlci1zbGF0ZS03MDAiPgogICAgICA8ZGl2PgogICAgICAgIDxoMSBjbGFzcz0idGV4dC0zeGwgZm9udC1ib2xkIHRyYWNraW5nLXRpZ2h0IG1iLTEiPlQvSC9SVVNUIEdQUzwvaDE+CiAgICAgICAgPHAgY2xhc3M9InRleHQtc2xhdGUtNDAwIHRleHQtc20gZm9udC1tZWRpdW0gdXBwZXJjYXNlIj5MaXZlIFRlbGVtZXRyeSBEYXNoYm9hcmQ8L3A+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2MDg+CiAgICAgICAgPHNwYW4gOmNsYXNzPSJpc0Nvbm5lY3RlZCA/ICd0ZXh0LWdyZWVuLTQwMCcgOiAndGV4dC1yZWQtNTAwJyI+CiAgICAgICAgICB7eyBpc0Nvbm5lY3RlZCA/ICdDT05ORUNURUQnIDogJ0RJU0NPTk5FQ1RFRCcgfX0KICAgICAgICA8L3NwYW4+CiAgICAgIDwvZGl2MDg+CiAgICA8L2hlYWRlcj4KCiAgICA8ZGl2IHYtaWY9ImxhdGVzdFRlbGVtZXRyeSIgY2xhc3M9ImdyaWQgZ3JpZC1jb2xzLTEgbWQ6Z3JpZC1jb2xzLTMgZ2FwLTYiPgogICAgICA8c2VjdGlvbiBjbGFzcz0iYmctc2xhdGUtODAwIHJvdW5kZWQteGwgcC02IGZsZXggZmxleC1jb2wgaXRlbXMtY2VudGVyIj4KICAgICAgICA8aDIgY2xhc3M9InRleHQteGwgbWItNCI+VHJ1c3QgSW5kZXg8L2gyPgogICAgICAgIDxkaXYgY2xhc3M9InRleHQtNXhsIGZvbnQtYm9sZCIgOmNsYXNzPSJsYXRlc3RUZWxlbWV0cnkudHJ1c3RfaW5kZXggPiA1MCA/ICd0ZXh0LWdyZWVuLTUwMCcgOiBndGV4dC1yZWQtNTAwJyI+CiAgICAgICAgICB7eyBsYXRlc3RUZWxlbWV0cnkudHJ1c3RfaW5kZXgudG9GaXhlZCgxKSB9fSUKICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJtdC00IHB4LTQgcHktMSByb3VuZGVkLWZ1bGwgdXBwZXJjYXNlIGJvcmRlciIgOmNsYXNzPSJsYXRlc3RUZWxlbWV0cnkubGFiZWwuaW5jbHVkZXMoJ2F1dGhlbnRpYycpID8gJ2JvcmRlci1ncmVlbi01MDAgdGV4dC1ncmVlbi01MDAnIDogJ2JvcmRlci1yZWQtNTAwIHRleHQtcmVkLTUwMCciPgogICAgICAgICAge3sgbGF0ZXN0VGVsZW1ldHJ5LmxhYmVsIH19IERldGVjdGlvbgogICAgICAgIDwvZGl2PgogICAgICA8L3NlY3Rpb24+CgogICAgICA8c2VjdGlvbiBjbGFzcz0ibWQ6Y29sLXNwYW4tMiBiZy1zbGF0ZS04MDAgcm91bmRlZC14bCBwLTYiPgogICAgICAgIDxoMiBjbGFzcz0idGV4dC14bCBtYi00Ij4xMyBUZWxlbWV0cnkgRmVhdHVyZXM8L2gyPgogICAgICAgIDxkaXYgY2xhc3M9ImdyaWQgZ3JpZC1jb2xzLTIgbWQ6Z3JpZC1jb2xzLTQgZ2FwLTQiPgogICAgICAgICAgPGRpdiB2LWZvcj0iaSBpbiAxMyIgOmtleT0iaSIgY2xhc3M9ImJnLXNsYXRlLTkwMCBwLTMgcm91bmRlZC1sZyBib3JkZXIgYm9yZGVyLXNsYXRlLTcwMCI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJ0ZXh0LXhzIHRleHQtc2xhdGUtNTAwIj5Ge3sgaSB9fTwvc3Bhbj48YnIvPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0idGV4dC1zbSBmb250LW1vbm8iPnt7IE51bWJlcihsYXRlc3RUZWxlbWV0cnlbJ2ZlYXR1cmVfJytpIGFzIGtleW9mIFRlbGVtZXRyeURhdGFdKS50b0ZpeGVkKDQpIH19PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvc2VjdGlvbj4KICAgIDwvZGl2PgogICAgCjwvbWFpbj4KPC90ZW1wbGF0ZT4K" | base64 -D > "/Users/jakubminorczyk/Documents/T:H:RUST GPS/Frontend/src/App.vue"
EOL
