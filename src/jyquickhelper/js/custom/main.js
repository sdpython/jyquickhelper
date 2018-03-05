define(['base/js/namespace'], 
       function(Jupyter) {

    var load_css = function () {
        var link = document.createElement("link");
        link.type = "text/css";
        link.rel = "stylesheet";
        link.href = require.toUrl("./jyquickhelper_custom.css");
        document.getElementsByTagName("head")[0].appendChild(link);
    };
    
    function load_ipython_extension() {
        
        load_css();
        
        var handler = function () {
            alert('This is an alert from jyquickhelper_custom extension!');
        };

        var action = {
            icon: 'fa-comment-o', // a font-awesome class used on buttons, etc
            help: 'Show an alert',
            help_index: 'zz',
            handler: handler
        };
        var prefix = 'my_extension';
        var action_name = 'show-alert';

        var full_action_name = Jupyter.actions.register(action, action_name, prefix);
        Jupyter.toolbar.add_buttons_group([full_action_name]);
        
        console.log('Custom javascript extension:', Jupyter.notebook);
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
