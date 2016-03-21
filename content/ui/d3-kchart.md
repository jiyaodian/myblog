Title: 用D3.js画K线图
Slug: k-chart-by-d3
Date: 2015-02-12 11:22:25
Tags: d3, ui
Category: ui
Author: jyd
Lang: zh
Summary: 用D3画K线图

### 前言

本来想用echart库来画k线图，无奈太复杂了，而且很难做成自己想要的样子。无奈之下看了下d3，发现原来这么好用，这么简单，几行代码就能把想表达的东西画出来了。大喜……

然后又想到已经好久没写博文了，就写下来吧。

### 准备
[D3 API参考文档](https://github.com/mbostock/d3/wiki)

首先，你得先对HTML、CSS、JS、SVG有一些了解，不了解的建议先去搜索些资料看看。当然，你也可以先往下看看，看到不懂的时候再搜索。

接着，当然就是安装D3啦, 到[D3官网](http://d3js.org/)看下怎么安装吧。其实就是下载代码，然后在页面中引入，也可以直接复制下面代码都页面中。
```html
<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
```

最后，新建个html文件，代码如下
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>d3 k-chart</title>
</head>
<body>

<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>

<script type="text/javascript">
//之后的代码都写在这里
</script>

</body>
</html>
```

要画k线图，首先得先有数据。
```javascript
    var dataset = [
        ['2011-12-16', 25.000, 24.900, 26.800, 26.440, 1171773, 3013978000.00],
        ['2011-12-19', 26.210, 26.000, 27.490, 26.960, 524161, 1393216000.00],
        ['2011-12-20', 27.100, 26.650, 27.590, 26.880, 274802, 744248000.00],
        ['2011-12-21', 27.140, 26.290, 27.650, 26.390, 221804, 599846800.00],
        ['2011-12-22', 25.960, 25.560, 27.200, 26.800, 147229, 386845500.00],
        ['2011-12-23', 26.520, 25.820, 27.170, 27.090, 126590, 337348500.00],
        ['2011-12-26', 26.710, 26.490, 27.320, 26.710, 74700, 200983900.00],
        ['2011-12-27', 26.450, 26.020, 29.380, 27.070, 139441, 385938100.00],
        ['2011-12-28', 26.470, 25.130, 27.420, 27.120, 107477, 284469300.00],
        ['2011-12-29', 26.610, 26.610, 28.300, 28.120, 99828, 277077400.00],
        ['2011-12-30', 27.970, 27.800, 28.690, 27.870, 113659, 320882300.00],
        ['2012-01-04', 27.920, 27.700, 28.550, 27.970, 76590, 215469100.00],
        ['2012-01-05', 27.940, 26.880, 28.420, 27.100, 89823, 248863800.00],
        ['2012-01-06', 26.600, 26.600, 28.210, 28.140, 61342, 168226600.00],
        ['2012-01-09', 28.090, 27.610, 29.550, 29.380, 67159, 192597700.00],
        ['2012-01-10', 29.380, 29.000, 30.300, 30.120, 84051, 250574200.00],
        ['2012-01-11', 29.950, 29.100, 30.200, 29.870, 47952, 142677200.00],
        ['2012-01-12', 29.620, 29.620, 30.950, 30.380, 55554, 168174300.00],
        ['2012-01-13', 30.480, 28.950, 30.580, 29.870, 49726, 147160100.00],
        ['2012-01-16', 29.500, 28.130, 29.770, 28.280, 36006, 105667100.00],
        ['2012-01-17', 28.580, 28.500, 30.920, 30.870, 91777, 271016900.00],
        ['2012-01-18', 30.540, 29.180, 30.900, 29.730, 64588, 195056000.00],
        ['2012-01-19', 29.730, 29.370, 30.600, 30.210, 38141, 115276000.00],
        ['2012-01-20', 30.100, 30.100, 32.220, 31.890, 66314, 207219200.00]
    ];

```
其中，每个字段分别是日期，开盘价、最低价、最高价、收盘价、交易量、交易金额。

### 只有开盘价和收盘价的k线图

好了，现在有数据了。那第一步先画什么呢？先根据开盘价和收盘价画那个矩形吧！
先来个简单的矩形。
```javascript
var svg = d3.select("body").append('svg').attr('width', 800).attr('height', 200);
svg.append('rect').attr('x', 10).attr('y', 10).attr('width', 100).attr('height', 100).attr('fill', 'red');
```
第一行代码会在body标签里面加入一个宽800px、高200px的SVG标签，这个可以认为是个画布，矩形要画在这个里面。

第二行代码就是在SVG标签里面加进去一个红色矩形框。

这里用到了三个函数，

* d3.select(): dom选择函数，可以根据标签、类、ID、属性等来选择。
* selection.append()：添加一个新元素到当前选择器中，这里是加到svg标签中，并返回新添加的标签选择器。
* selection.attr()：设置当前选择器的属性值。rect包含x、y、width、height等属性，分别指定矩形的坐标和宽高，具体请参考SVG相关文档(给出链接)。

![矩形](/images/d3-rect.png)

太简单了？那就直接进入主题吧。先贴代码~

```javascript
var w = 500, h = 200;
var svg = d3.select("body").append('svg').attr('width', w).attr('height', h);
var price_min = d3.min(dataset, function (d) {
    return d3.min(d.slice(1, 5))
});
var price_max = d3.max(dataset, function (d) {
    return d3.max(d.slice(1, 5))
});
var yscale = d3.scale.linear()
    .domain([price_min, price_max])
    .range([0, h]);
var rect_attr = {
    'x': function (d, i) {
        return i * (w / dataset.length);
    },
    'y': function (d, i) {
        return h - yscale(d3.max([d[1], d[4]]));
    },
    'width': function (d, i) {
        return w / dataset.length - 4;
    },
    'height': function (d, i) {
        return Math.abs(yscale(d[1]) - yscale(d[4]));
    },
    "fill": function (d) {
        if (d[1] < d[4]) return 'red';
        else return 'green';
    }
};
svg.selectAll('rect').data(dataset).enter().append('rect').attr(rect_attr);
```

效果：
![矩形2](/images/d3-rect2.png)

怎样？有点感觉了吧？
来解释下代码吧~

a. 新建个画布。
```javascript
var svg = d3.select("body").append('svg').attr('width', w).attr('height', h);
```
b. 取得所有价格的最大值和最小值，我用了d3.min和d3.max函数。当然，这里完全可以来两个for循环找出最大值和最小值的。
```javascript
    var price_min = d3.min(dataset, function (d) {
            return d3.min(d.slice(1, 5))
        });
        var price_max = d3.max(dataset, function (d) {
            return d3.max(d.slice(1, 5))
        });
```

c. 定义归一化函数: yscale。 函数yscale()的功能就是把数字区间[price_min, price_max]映射到区间[0, h]上。 
```javascript
  var yscale = d3.scale.linear()
        .domain([price_min, price_max])
        .range([0, h]);
```
假设price_min = 100, price_max=200, h=10.  那么

* yscale(100) => 0
* yscale(200) => 10
* yscale(150) => 5
* yscale(120) => 2
* yscale(122) => 2.2

为什么要有这么一个映射函数呢？因为我们要画的是k线图，图中的y轴只需要能显示最低价格和最高价格就行了，没必要从0开始，所以要把价格映射到(0, h)区间内，方便显示。

d. 定义矩形的属性值。

* x、y确定矩形的坐标。SVG的坐标系（0,0)点在左上角，横轴是x, 纵轴是y。
* width、height确定矩形的宽和高
* fill则定义矩形的颜色
 
```javascript
var rect_attr = {
        'x': function (d, i) {
            return i * (w / dataset.length);
        },
        'y': function (d, i) {
            return h - yscale(d3.max([d[1], d[4]]));
        },
        'width': function (d, i) {
            return w / dataset.length - 4;
        },
        'height': function (d, i) {
            return Math.abs(yscale(d[1]) - yscale(d[4]));
        },
        "fill": function (d) {
            if (d[1] < d[4]) return 'red';
            else return 'green';
        }
    };
```
当d3在设置矩形属性值的时候，它会调用我们定义的函数 function(d, i),这里的d对应一个矩形的数据【也是dataset一条数据】，i则是这条数据的编号，从0开始，最大值是dataset.length-1。

* 属性 x:  i * (w / dataset.length), 这样可以矩形均匀的分布在画布中。
* 属性 y: h - yscale(d3.max(d[1], d[4])), 因为坐标(0, 0)点是在左上角的，所以
* 属性 width: w / dataset.length - 4, 你可以试试把-4去掉，看看效果。
* 属性 height: Math.abs(yscale(d[1]) - yscale(d[4]))
* 属性 fille: 当开盘价d[1]小于收盘价d[4]的时候为红色，否则绿色。

e. 根据dataset数据生成矩形，并设定个个矩形的属性值。
```javascript
svg.selectAll('rect').data(dataset).enter().append('rect').attr(rect_attr);
```

### 有最高价、最低价的K线图
效果
![初版k线图](/images/d3-k1.png)
怎样，更有感觉了吧~
其实只需要根据最高价和最低价画直线就行了，SVG里面直线的标签是 line。 所以依样画葫芦，只需要在之前代码后面再加上下面这个代码就行了~
```javascript
data_cnt = dataset.length;
barPadding = 4;
svg.selectAll('line')
    .data(dataset)
    .enter()
    .append('line')
    .attr({
        'x1': function (d, i) {
            return i * (w / data_cnt) + (w / data_cnt - barPadding) / 2;
        },
        'x2': function (d, i) {
            return i * (w / data_cnt) + (w / data_cnt - barPadding) / 2;
        },
        'y1': function (d, i) {
            return h - yscale(d3.max(d.slice(1, 5)));
        },
        'y2': function (d, i) {
            return h - yscale(d3.min(d.slice(1, 5)));
        },
        "stroke": function (d) {
            if (d[1] < d[4]) return 'red';
            else return 'green';
        }
    });
```


文章还是不要太长了，这篇就先到这吧~下一篇继续讲~

最后附上全部代码(对代码风格做了点修改)：
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>d3 k-chart</title>
</head>
<body>

<script src="http://libs.useso.com/js/d3/3.4.8/d3.min.js" charset="utf-8"></script>

<script type="text/javascript">
    var dataset = [
        ['2011-12-16', 25.000, 24.900, 26.800, 26.440, 1171773, 3013978000.00],
        ['2011-12-19', 26.210, 26.000, 27.490, 26.960, 524161, 1393216000.00],
        ['2011-12-20', 27.100, 26.650, 27.590, 26.880, 274802, 744248000.00],
        ['2011-12-21', 27.140, 26.290, 27.650, 26.390, 221804, 599846800.00],
        ['2011-12-22', 25.960, 25.560, 27.200, 26.800, 147229, 386845500.00],
        ['2011-12-23', 26.520, 25.820, 27.170, 27.090, 126590, 337348500.00],
        ['2011-12-26', 26.710, 26.490, 27.320, 26.710, 74700, 200983900.00],
        ['2011-12-27', 26.450, 26.020, 29.380, 27.070, 139441, 385938100.00],
        ['2011-12-28', 26.470, 25.130, 27.420, 27.120, 107477, 284469300.00],
        ['2011-12-29', 26.610, 26.610, 28.300, 28.120, 99828, 277077400.00],
        ['2011-12-30', 27.970, 27.800, 28.690, 27.870, 113659, 320882300.00],
        ['2012-01-04', 27.920, 27.700, 28.550, 27.970, 76590, 215469100.00],
        ['2012-01-05', 27.940, 26.880, 28.420, 27.100, 89823, 248863800.00],
        ['2012-01-06', 26.600, 26.600, 28.210, 28.140, 61342, 168226600.00],
        ['2012-01-09', 28.090, 27.610, 29.550, 29.380, 67159, 192597700.00],
        ['2012-01-10', 29.380, 29.000, 30.300, 30.120, 84051, 250574200.00],
        ['2012-01-11', 29.950, 29.100, 30.200, 29.870, 47952, 142677200.00],
        ['2012-01-12', 29.620, 29.620, 30.950, 30.380, 55554, 168174300.00],
        ['2012-01-13', 30.480, 28.950, 30.580, 29.870, 49726, 147160100.00],
        ['2012-01-16', 29.500, 28.130, 29.770, 28.280, 36006, 105667100.00],
        ['2012-01-17', 28.580, 28.500, 30.920, 30.870, 91777, 271016900.00],
        ['2012-01-18', 30.540, 29.180, 30.900, 29.730, 64588, 195056000.00],
        ['2012-01-19', 29.730, 29.370, 30.600, 30.210, 38141, 115276000.00],
        ['2012-01-20', 30.100, 30.100, 32.220, 31.890, 66314, 207219200.00]
    ];
    var dataCnt = dataset.length;
    var w = 500, h = 200;
    var barPadding = 4;
    var svg = d3.select("body").append('svg').attr('width', w).attr('height', h);
    var priceMin = d3.min(dataset, function (d) {
        return d3.min(d.slice(1, 5))
    });
    var priceMax = d3.max(dataset, function (d) {
        return d3.max(d.slice(1, 5))
    });

    var yscale = d3.scale.linear()
        .domain([priceMin, priceMax])
        .range([0, h]);

    var rectAttr = {
        'x': function (d, i) {
            return i * (w / dataCnt)
        },
        'y': function (d, i) {
            return h - yscale(d3.max([d[1], d[4]]));
        },
        'width': function (d, i) {
            return w / dataCnt - barPadding;
        },
        'height': function (d, i) {
            return Math.abs(yscale(d[1]) - yscale(d[4]));
        },
        "fill": function (d) {
            if (d[1] < d[4]) return 'red';
            else return 'green';
        }
    };
    svg.selectAll('rect').data(dataset).enter().append('rect').attr(rectAttr);

    svg.selectAll('line')
        .data(dataset)
        .enter()
        .append('line')
        .attr({
            'x1': function (d, i) {
                return i * (w / dataCnt) + (w / dataCnt - barPadding) / 2;
            },
            'x2': function (d, i) {
                return i * (w / dataCnt) + (w / dataCnt - barPadding) / 2;
            },
            'y1': function (d, i) {
                return h - yscale(d3.max(d.slice(1, 5)));
            },
            'y2': function (d, i) {
                return h - yscale(d3.min(d.slice(1, 5)));
            },
            "stroke": function (d) {
                if (d[1] < d[4]) return 'red';
                else return 'green';
            }
        });
</script>

</body>
</html>
```

