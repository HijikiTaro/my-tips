
```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "Java List ",
  "data": {
    "values": [
      {"Java": "JRE-1.1", "ms": 451},
      {"Java": "J2SE-1.2", "ms": 484},
      {"Java": "J2SE-1.3", "ms": 497},
      {"Java": "J2SE-1.4", "ms": 600},
      {"Java": "J2SE-1.5", "ms": 491},
      {"Java": "JavaSE-1.6", "ms": 458},
      {"Java": "JavaSE-1.7", "ms": 461},
      {"Java": "JavaSE-1.8", "ms": 466},
      {"Java": "JavaSE-9", "ms": 658},
      {"Java": "JavaSE-10", "ms": 534},
      {"Java": "JavaSE-11", "ms": 513},
      {"Java": "JavaSE-12", "ms": 380},
      {"Java": "JavaSE-13", "ms": 414}
    ]
  },
  "encoding": {
    "y": {"field": "Java", "type": "ordinal"},
    "x": {"field": "ms", "type": "quantitative", "scale": {"padding": 10}}
  },
  "layer": [{
    "mark": "bar"
  }, {
    "mark": {
      "type": "text",
      "align": "left",
      "baseline": "middle",
      "dx": 3
    },
    "encoding": {
      "text": {"field": "ms", "type": "quantitative"}
    }
  }]
}
```