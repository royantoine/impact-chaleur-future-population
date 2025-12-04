
// Appel du fond de carte
mapboxgl.accessToken = 'pk.eyJ1IjoibGVwbGFuc3R1ZGlvIiwiYSI6ImNsdWNnMTRpNDEzeXoyanFuOGdxbm1kOXIifQ.bGLWHO7ce0M37dJCnJ0s3w';
const bounds = [[-10, 36], [15, 56]];
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/leplanstudio/cmipzcx7k00ng01sbenbha21p',
    center: [2, 46.8],
    zoom: 5.1,
    minZoom: 5,
    maxZoom: 12,
    maxBounds: bounds,
});

// Début des couches
map.on('load', () => {

    // ############# COUCHE demog-climat  ##################################################
    map.addSource('demog-climat', {
        type: 'geojson',
        data: 'DATA/points1km_projDemog_Climat_v3.geojson'
    });

     map.addLayer({
        'id': '65P_2050',
        'type': 'circle',
        'source': 'demog-climat',
        'layout': {},
        'paint': {
            'circle-opacity': 0.8,
            'circle-color': [
                        'interpolate',
                    ['exponential', 2], // Set the interpolation type
                    ['get','sc_27_n_heatwaves_days_min20_max35'],
                    1,
                    '#006bd7',
                    5,
                    '#00a2c7',
                    10,
                    '#eeea00',
                    15,
                    '#ee9f00',
                    30,
                    '#ee4b00',
                    50,
                    '#e10000',
                    60,
                    '#730000'
                    ],           
            // 'circle-radius': ['/', ['sqrt', ['/', ['get', 'S1_pop65p_2050'], 3.14]], 5]

            'circle-radius':[
        "interpolate", ["linear"], ["zoom"],
        // when zoom is 0, set each feature's circle radius to the value of its "rating" property
        5, ['/', ['sqrt', ['/', ['get', 'S1_pop65p_2050'], 3.14]], 8],
        // when zoom is 10, set each feature's circle radius to four times the value of its "rating" property
        12,  ['/', ['sqrt', ['/', ['get', 'S1_pop65p_2050'], 3.14]], 3]
    ]
        }
    });

     
    map.addLayer({
        'id': '65P_today',
        'type': 'circle',
        'source': 'demog-climat',
        'layout': {},
        'paint': {
            'circle-opacity': 0,
            'circle-color': [
                        'interpolate',
                    ['exponential', 2],
                    ['get','sc_today_n_heatwaves_days_min20_max35'],
                    1,
                    '#006bd7',
                    5,
                    '#00a2c7',
                    10,
                    '#ebe970',
                    15,
                    '#ee9f00',
                    30,
                    '#ee4b00',
                    50,
                    '#e10000',
                    60,
                    '#730000'
                    ],           
            'circle-radius': ['/', ['sqrt', ['/', ['get', 'pop65p_2019'], 3.14]], 5]
        }
    });
   
    // Fin des couches 
});

// ##########################################################################################
// ########## Affichage des couches au clic sur la liste 

// ########## Affichage 65P_today ################################################
document.getElementById('lien_65P_today').addEventListener('click', () => {
    const circleOpacity = map.getPaintProperty('65P_today', 'circle-opacity');
    if (circleOpacity === 0) {
        map.setPaintProperty('65P_today', 'circle-opacity', 0.8); this.className = '';
        document.getElementById("oeil_65P_today").innerHTML = '<i class="far fa-thin fa-eye" style="color:#D38D31; font-weight: 800;"></i>';
    } else {
        this.className = 'active'; map.setPaintProperty('65P_today', 'circle-opacity', 0);
        document.getElementById("oeil_65P_today").innerHTML = '<i class="far fa-thin fa-eye-slash"></i>';
    };
});

// ########## Affichage 65P_2050 ################################################
document.getElementById('lien_65P_2050').addEventListener('click', () => {
    const circleOpacity = map.getPaintProperty('65P_2050', 'circle-opacity');
    if (circleOpacity === 0) {
        map.setPaintProperty('65P_2050', 'circle-opacity', 0.8); this.className = '';
        document.getElementById("oeil_65P_2050").innerHTML = '<i class="far fa-thin fa-eye" style="color:#D38D31; font-weight: 800;"></i>';
    } else {
        this.className = 'active'; map.setPaintProperty('65P_2050', 'circle-opacity', 0);
        document.getElementById("oeil_65P_2050").innerHTML = '<i class="far fa-thin fa-eye-slash"></i>';
    };
});

//////////////////////////////////////////////////////        
///////////  POPUP  //////////////////////////////////
const popup = new mapboxgl.Popup({
                    closeButton: false,
                    closeOnClick: false
                });

        let Idcarreau = null;

    
        map.on('mousemove', ("65P_2050"), (e) => {
                    map.getCanvas().style.cursor = 'pointer';
                    if (Idcarreau) {
                        map.removeFeatureState({ source: 'demog-climat', id: Idcarreau });
                    }
                    Idcarreau = e.features[0].id;
                    map.setFeatureState({ source: 'demog-climat', id: Idcarreau }, { hover: true });
                    // Contenu de la popup
                    const EPCI = e.features[0].properties.NOM_EPCI;
                    const DEP = e.features[0].properties.NOM_DEP;
                    const DEMOG = e.features[0].properties.texte_demog;
                    const CLIMAT = e.features[0].properties.texte_climat;

                    popup.setLngLat(e.lngLat).setHTML(DEMOG+'</br>'+CLIMAT+'</br><span style="color:#a3a3a3; font-size: 13px">(EPCI : '+EPCI+' - Département : '+DEP+')</i>'
                    ).addTo(map);
            });
        map.on('mouseleave', ("65P_2050"), () => {  
            if (Idcarreau) {
                map.setFeatureState({ source: 'demog-climat', id: Idcarreau }, { hover: false });
            }
            Idcarreau = null;
            map.getCanvas().style.cursor = '';
            popup.remove();
        });