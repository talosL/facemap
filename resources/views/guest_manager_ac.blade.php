@extends('layouts.conapp')

<body style="background: #f6f5fa;">
@if(!empty(session('success')))
    　　<div class="alert alert-success alert-dismissable" role="alert">
        <button type="button" class="close" data-dismiss="alert"
                aria-hidden="true">
            &times;
        </button>
        　　　　{{session('success')}}
        　　</div>
@endif
@if(!empty(session('fail')))
    　　<div class="alert alert-danger  alert-dismissable" role="alert">
        <button type="button" class="close" data-dismiss="alert"
                aria-hidden="true">
            &times;
        </button>
        　　　　{{session('fail')}}
        　　</div>
@endif
<!--content S-->
<div class="super-content">
    <div class="superCtab">
        <div class="ctab-title clearfix"><h3>访客管理</h3>
        </div>

        <div class="ctab-Main">
            <div class="ctab-Main-title">
                <ul class="clearfix">
                    <li class="cur"><a href="{{url('guest_manager_ac')}}">已识别访客</a></li>
                    <li><a href="{{url('guest_manager_str')}}">陌生访客</a></li>
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
                                    <a data-toggle="modal" data-target="#{{$stranger->face_id}}">
                                        <img class=""
                                             src="data:image/jpeg;base64,{{base64_encode($stranger->face_path)}}"
                                             alt="{{$stranger->face_name}}" height="70%"
                                             style="padding: 4px;background-color: #fff;border: 1px solid #ddd;border-radius: 4px;">
                                        <p>姓名：{{$stranger->face_name}}</p>
                                    </a>
                                </div>

                                @endforeach
                            </div>
                        </div>
                    </div>
<div style="text-align: center">{{ $strangers->links() }}</div>

                </div>
            </div>
        </div>
        <!--main-->
    </div>
</div>
<div>
    @foreach ($strangers as $stranger)
    <div class="modal fade" id="{{$stranger->face_id}}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
         aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title" id="myModalLabel" style="float: left">修改信息</h4>
                </div>
                <form action="{{url('change_ac')}}" method="post">
                    <div class="modal-body">
                        <div class="col-sm-10">
                            <input type="text" name="face_token" class="form-control" id="disabledInput"
                                   value="{{$stranger->face_token}}" style="display: none">

                            <span>face_token:</span><input type="text" name="face_tk" class="form-control" id="disabledInput"
                                                           value="{{$stranger->face_token}}" disabled>
                            <br>
                        </div>
                        <div class="col-sm-10">
                            <span>name:</span><input type="text" name="name" class="form-control" id=""
                                                     placeholder="{{$stranger->face_name}}">

                        </div>

                        {{--                            <div class="col-sm-10">--}}
                            {{--                                <br>--}}
                            {{--                                <input type="text" name="age" class="form-control" id=""--}}
                                                                       {{--                                       placeholder="{{$stranger->face_age}}">--}}
                            {{--                            </div>--}}


                    </div>
                    <div class="modal-footer" style="margin-top: 135px">
                        <input type="button" class="btn btn-default" data-dismiss="modal" value="关闭">
                        <input type="submit" class="btn btn-primary" value="提交更改">
                    </div>
                </form>
            </div><!-- /.modal-content -->
        </div><!-- /.modal -->
    </div>

    @endforeach
</div>


</body></html>

