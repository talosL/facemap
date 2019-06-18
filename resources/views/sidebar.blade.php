@extends('layouts.conapp')

<body>
	<!--side S-->

	<div class="super-side-menu">
		<div class="side-menu">
			<ul>
				<li class=""><a href="{{url('capture')}}" target="Mainindex"><i class="ico-1"></i>打开</a></li>
				<li ><a href="{{url('today_ac')}}" target="Mainindex"><i class="ico-2"></i>今日来访</a></li>
				<li ><a href="{{url('history_ac')}}" target="Mainindex"><i class="ico-3"></i>历史来访</a></li>
				<li ><a href="{{url('guest_manager_ac')}}" target="Mainindex"><i class="ico-5"></i>访客管理</a></li>
				<li><a href="{{url('uploadimg')}}" target="Mainindex"><i class="ico-4"></i>照片上传</a></li>
				<li><a href="{{url('cam_history')}}" target="Mainindex"><i class="ico-7"></i>操作记录</a></li>
				<li><nav >
						<div class="container" >
							<div >
								<!-- Right Side Of Navbar -->
								<ul >
									<!-- Authentication Links -->
										<li >

											<a id="navbarDropdown"  href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
												<span class="glyphicon glyphicon-user"></span>
												{{ Auth::user()->name }} <span class="caret"></span>
											</a>

											<div class="dropdown-menu dropdown-menu-left" aria-labelledby="navbarDropdown">
												<a class="dropdown-item" href="{{ route('logout') }}" target="_parent"
												   >
													{{ __('Logout') }}
												</a>


											</div>
										</li>
								</ul>
							</div>
						</div>
					</nav></li>
			</ul>
		</div>

	</div>
    <script type="text/javascript">
        $(function(){
            $('.side-menu li').click(function(){
                $(this).addClass('on').siblings().removeClass('on');
            })
        })
    </script>

</body></html>