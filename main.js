var container = document.querySelector('#view'),
    loader = vega.loader(),
    renderType = 'svg',
    runtime = null,
    spec = null,
    view = null;

var select = document.querySelector('#specs');

select.addEventListener('change', function() {
  load(select.options[select.selectedIndex].value);
});

var render = document.querySelector('#render');

render.addEventListener('change', function() {
  renderType = render.options[render.selectedIndex].value;
  if (view) view.renderer(renderType).run();
});

loader.load('specs.json')
  .then(function(data) {
    // load manifest of test specifications
    JSON.parse(data).forEach(function(name) {
      var opt = document.createElement('option');
      opt.setAttribute('value', name);
      opt.textContent = name;
      select.appendChild(opt);
    });
  })
  .then(function() {
    // if query string is present, try to load spec
    if (location.search) load(location.search.slice(1));
  });

function load(name) {
  if (!name) {
    if (view) view.finalize(), container.innerHTML = '';
    return;
  }
  // update select widget state
  select.selectedIndex = 0;
  for (var i=0, n=select.options.length; i<n; ++i) {
    if (select.options[i].value === name) {
      select.selectedIndex = i; break;
    }
  }
  // load vega spec, then visualize it
  loader.load(url = './spec/' + name)
    .then(function(data) {
      console.log('LOADED', url);
      var spec = JSON.parse(data);
      var vgSpec = name.indexOf('vl.json') > -1 ? vl.compile(spec).spec : spec;
      visualize(spec = vgSpec);
    })
    .catch(function(err) {
      console.error(err, err.stack);
    });
}

function visualize(spec) {
  if (view) view.finalize(); // finalize existing view
  view = new vega.View(runtime = vega.parse(spec))
    .logLevel(vega.Warn)
    .renderer(renderType)
    .initialize(container)
    .hover()
    .run();
}