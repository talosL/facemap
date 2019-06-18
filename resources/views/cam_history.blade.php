@extends('layouts.conapp')

<body style="background: #f6f5fa;">

<!--content S-->

<div class="super-content">
    <div class="superCtab">
        <div class="ctab-title clearfix"><h3>操作记录</h3>
        </div>

        <div class="ctab-Main">
            <div class="ctab-Main-title">
                <ul class="clearfix">
                    <li class="cur"><a href="{{url('cam_history')}}">拍照记录</a></li>
                    <li><a href="{{url('upload_history')}}">上传记录</a></li>
                </ul>
            </div>
            <div class="superCtab superCtabBot">
                <div class="ctab-Mian-cont">

                    <div class="Mian-cont-wrap">
                        <div class="container">
                            <div class="row">
                                @foreach ($strangers as $stranger)
                                    <div class="col-md-3 col-sm-3 col-xs-3"
                                         style="padding-top:6px;height: 200px;border: 0px">
                                        <a data-toggle="modal" data-target="#{{$stranger->photo_id}}">
                                            <img class=""
                                                 src="data:image/jpeg;base64,{{base64_encode($stranger->face_path)}}"
                                                 alt="{{$stranger->time}}" height="70%"
                                                 style="padding: 4px;background-color: #fff;border: 1px solid #ddd;border-radius: 4px;">
                                            <p>姓名：{{$stranger->face_name1}}{{$stranger->face_name2}}<br>拍照时间：{{$stranger->time}}</p>
                                        </a>
                                    </div>

                                @endforeach
                            </div>
                        </div>
                    </div>

                    {{ $strangers->links() }}
                </div>
            </div>
        </div>
        <!--main-->
    </div>
</div>
<div>
    @foreach ($strangers as $stranger)
        <div class="modal fade" id="{{$stranger->photo_id}}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
             aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title" id="myModalLabel" style="float: left">修改信息</h4>
                    </div>
                    <form action="/cam_photo?act=1" method="get">
                        <div class="modal-body">
                            <input type="text" name="face_token" class="form-control" id="disabledInput"
                                   value="{{$stranger->photo_id}}" style="display: none">
                            @if($stranger->face_token1!=null)
                            <div class="col-sm-10">
                                <span>face_token1:</span><input type="text" name="face_tk" class="form-control" id="disabledInput"
                                                               value="{{$stranger->face_token1}}" disabled>
                                <br>
                            </div>
                            <div class="col-sm-10">
                                <span>name1:</span><input type="text" name="name" class="form-control" id=""
                                                         placeholder="{{$stranger->face_name1}}">
                            </div>
                                @else
                                <div class="col-sm-10">
                                    <span>无信息可修改</span>
                                </div>
                            @endif
                            @if($stranger->face_token2 != null)
                            <div class="col-sm-10">
                                <span>face_token2:</span><input type="text" name="face_tk" class="form-control" id="disabledInput"
                                                               value="{{$stranger->face_token2}}" disabled>
                                <br>
                            </div>
                            <div class="col-sm-10">
                                <span>name2:</span><input type="text" name="name" class="form-control" id=""
                                                         placeholder="{{$stranger->face_name2}}">
                            </div>
                            @endif

                            {{--                            <div class="col-sm-10">--}}
                            {{--                                <br>--}}
                            {{--                                <input type="text" name="age" class="form-control" id=""--}}
                            {{--                                       placeholder="{{$stranger->face_age}}">--}}
                            {{--                            </div>--}}


                        </div>
                        <div class="modal-footer" style="margin-top: 135px">
                            <input type="button" class="btn btn-default" data-dismiss="modal" value="关闭">
                            @if($stranger->face_token1!=null)
                            <input type="submit" class="btn btn-primary" value="提交更改">
                                @endif
                        </div>
                    </form>
                </div><!-- /.modal-content -->
            </div><!-- /.modal -->
        </div>

    @endforeach
</div>


</body></html>

