/*****************************************************************************
 * FILE:      Leaflet Map Module for SWE web app
 * AUTHOR:    Karnesh Jain
 *****************************************************************************/

/*****************************************************************************
 *                      LIBRARY WRAPPER
 *****************************************************************************/

var LEAFLET_MAP = (function() {
    "use strict"; // And enable strict mode for this library

    /************************************************************************
    *                      MODULE LEVEL / GLOBAL VARIABLES
    *************************************************************************/
    var public_interface,                           // Object returned by the module
        m_map;                                              // The Leaflet Map
    var m_layer_meta,        // Map of layer metadata indexed by variable
        m_curr_dataset,      // The current selected dataset
        m_curr_variable,     // The current selected variable/layer
        m_curr_style,        // The current selected style
        m_curr_wms_url;      // The current WMS url

    /************************************************************************
    *                    PRIVATE FUNCTION DECLARATIONS
    *************************************************************************/
    // Map Methods
    var init_map;
    // Control Methods
    var init_controls, update_variable_control, update_style_control;


    /************************************************************************
    *                    PRIVATE FUNCTION IMPLEMENTATIONS
    *************************************************************************/
    // Map Methods
    init_map = function() {
        // Create Map
        m_map = L.map('leaflet-map', {
            zoom: 3,
            center: [0, 0],
            fullscreenControl: true,
        });

        // Add Basemap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(m_map);
    };

    // Control Methods
    init_controls = function() {
        console.log('Initializing controls...');
    };

    // Query the current WMS for available layers and add them to the variable control
    update_variable_control = function() {
        console.log('Updating variable control...');
    };

    // Update the available style options on the style control
    update_style_control = function() {
        console.log('Updating style control...');
    };

    /************************************************************************
    *                        DEFINE PUBLIC INTERFACE
    *************************************************************************/
    /*
     * Library object that contains public facing functions of the package.
     * This is the object that is returned by the library wrapper function.
     * See below.
     * NOTE: The functions in the public interface have access to the private
     * functions of the library because of JavaScript function scope.
     */
    public_interface = {};

    /************************************************************************
    *                  INITIALIZATION / CONSTRUCTOR
    *************************************************************************/

    // Initialization: jQuery function that gets called when
    // the DOM tree finishes loading
    $(function() {
        init_map();
        init_controls();
    });

    return public_interface;

}()); // End of package wrapper
