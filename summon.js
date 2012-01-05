var quiet = true;
var snaps = false;
var page;

var old = true;
function start() {
    onload(searched);
    var args = {
        'tbm': 'isch',
        'q': phantom.args.join(' ')
    };
    if (old) args['sout'] = 1;
    page.open('http://www.google.com/search?' + urlencode(args));
}

function searched() {
    var grid_class = old ? 'images_table': 'rg_li';
    var url = evaluate(function(grid_class) {
        var rg = document.getElementsByClassName(grid_class)[0];
        // We could return the img src, width and height, and render it
        var a = rg.getElementsByTagName('a')[0];
        return a.href;
    }, grid_class);
    url = url || '';

    var imgurl = url.match(/imgurl\x3d(.*?)\x26/);
    if (!imgurl) {
      console.log('UNKNOWN THING');
      phantom.exit();
    }

    onload(shortened);
    page.open('http://tinyurl.com/api-create.php?url=' + imgurl[1]);
}

function shortened() {
    var url = page.evaluate(function() {
      return document.body.innerText;
    });
    console.log('SUMMONED ' + url);
    phantom.exit();
}




try {
    run();
} catch(e) {
    if (!quiet) console.log('exception> ' + e);
    phantom.exit();
}

function run() {

    if (phantom.args.length != 1) {
        if (!quiet) {
            console.log('Usage: ' + phantom.scriptName + ' [args]');
        }
        phantom.exit();
    } else {
        page = require('webpage').create();
        if (!quiet) {
            page.onConsoleMessage = function(msg) {
                console.log('console> ' + msg);
            };
            page.onAlert = function(msg) {
                console.log('alert> ' + msg);
                phantom.exit()
            };
        }
        page.viewportSize = { width: 800, height: 400 };

        start();
    }
}

var snapshotNo = 0;
function takeSnapshot() {
    if (snaps) page.render('snap' + snapshotNo++ + '.png');
}

function onload(f) {
    function _onload(status) {
        if (status !== 'success') {
            if (!quiet) console.log('Unable to load page');
            phantom.exit();
        } else {
            window.setTimeout(function() {
                takeSnapshot();
                f();
            }, 0);
        }
    }
    page.onLoadFinished = _onload;
}

function urlencode(o) {
  var qs = [];
  for (var k in o) qs.push(k + '=' + encodeURIComponent(o[k]));
  return qs.join('&');
}

function evaluate(func) {
    var args = [].slice.call(arguments, 1);
    var str = 'function() { return (' + func.toString() + ')(';
    for (var i = 0, l = args.length; i < l; i++) {
        var arg = args[i];
        if (/object|string/.test(typeof arg)) {
            // extra stringify to allow apostrophes
            str += 'JSON.parse(' + JSON.stringify(JSON.stringify(arg)) + '),';
        } else {
            str += arg + ',';
        }
    }
    str = str.replace(/,$/, '); }');
    return page.evaluate(str);
}

