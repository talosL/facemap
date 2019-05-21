@extends('layouts.conapp')

<body style="background: #f6f5fa;">

<!--content S-->
<div class="super-content RightMain" id="RightMain">
    <div class="superCtab">
        <div class="ctab-title clearfix"><h3>今日访客</h3>
        </div>
        <div class="ctab-Main">
            <div class="ctab-Main-title">
                <ul class="clearfix">
                    <li><a href="{{url('today_ac')}}">已识别访客</a></li>
                    <li class="cur"><a href="{{url('today_str')}}">陌生访客</a></li>
                </ul>
            </div>

            <div class="ctab-Mian-cont">

                <div class="Mian-cont-wrap">
                    <div class="container">
                        <div class="row">
                            @foreach ($strangers as $stranger)
                                <div class="col-md-3" style="padding-top:6px;height: 200px;border: 0px">
                                    <img class="" src="data:image/jpeg;base64,{{base64_encode($stranger->face_path)}}"
                                         alt="{{$stranger->time}}" height="85%"
                                         style="padding: 4px;background-color: #fff;border: 1px solid #ddd;border-radius: 4px;">
                                    <br>
                                    <p>来访时间：{{$stranger->time}}</p>
                                </div>

                            @endforeach
                        </div>
                    </div>

                    {{ $strangers->links() }}
                </div>
            </div>
        </div>
    </div>
    <!--main-->

</div>
<!--content E-->
<!--点击修改弹出层-->
<div class="layuiBg" style="display: none; height: 757px;"></div><!--公共遮罩-->
<!--点击添加分类弹出-->
<div class="addFeileibox layuiBox">
    <div class="layer-title clearfix"><h2>添加分类</h2><span class="layerClose"></span></div>
    <div class="layer-content">
        <div class="aFllink clearfix" style="margin-top: 38px;"><span>二级栏目：</span><input type="text" value=""></div>
        <div class="aFlBtn"><input type="button" value="保存" class="saveBtn"></div>
    </div>
</div>
<!--栏目管理-->
<div class="Columnbox hdColumnbox layuiBox" style="left: 476.5px; top: 261.5px; display: none;">
    <div class="layer-title clearfix"><h2>栏目管理</h2><span class="layerClose"></span></div>
    <div class="layer-content">
        <ul class="colu-title clearfix">
            <li class="li-1">栏目名称</li>
            <li class="li-2">英文名称</li>
            <li class="li-5">栏目类型</li>
            <li class="li-3">操作</li>
            <li class="li-4">同步开关</li>
        </ul>
        <div class="colu-list">
            <ul class="colu-cont clearfix active">
                <li class="li-1"><i class="ico"></i>活动发布</li>
                <li class="li-2">English</li>
                <li class="li-5">列表页</li>
                <li class="li-3"><a href="javascript:;" class="colu-xg">修改</a></li>
                <li class="li-4"><input type="checkbox" id="checkbox_d1" class="chk_4"><label for="checkbox_d1"></label>
                </li>
            </ul>
            <div class="colunext" style="display: block;">
                <ul class="colu-next clearfix">
                    <li class="li-1"><i class="ico"></i>公司活动</li>
                    <li class="li-2"></li>
                    <li class="li-5">列表页</li>
                    <li class="li-3"><a href="javascript:;" class="colu-xg">修改</a></li>
                </ul>
                <ul class="colu-next clearfix">
                    <li class="li-1"><i class="ico"></i>团队活动</li>
                    <li class="li-2"></li>
                    <li class="li-5">列表页</li>
                    <li class="li-3"><a href="javascript:;" class="colu-xg">修改</a></li>
                </ul>
            </div>
        </div><!--新闻动态-->

    </div>
</div>
<!--栏目管理－修改-->
<div class="ColumnXgbox layuiBox">
    <div class="layer-title clearfix"><h2>添加分类</h2><span class="layerClose"></span></div>
    <div class="layer-content">
        <div class="aFllink clearfix"><span>修改名称：</span><input type="text" value=""></div>
        <div class="aFllink clearfix"><span>英文名称：</span><input type="text" value=""></div>
        <div class="aFlBtn"><input type="button" value="保存" class="saveBtn"></div>
    </div>
</div>


</body></html>
