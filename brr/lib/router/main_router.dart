import 'package:brr/view/location_write_page/location_write_page_view.dart';
import 'package:brr/view/history_page/history_page_view.dart';
import 'package:brr/view/mypage_page/mydata_page_view.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:brr/view/main_page/main_page_view.dart';
import 'package:brr/view/match_list_page/match_list_view.dart';
import 'package:brr/layout/main_layout.dart';
import 'package:brr/view/mypage_page/mypage_page_view.dart';
import 'package:brr/view/schedule_page/schedule_page_view.dart';
import 'package:brr/view/matching_page/fast_matching_view_page.dart';
import 'package:brr/view/sign_up_page/sign_up_view.dart';
import 'package:brr/view/login_page/login_page_view.dart';
import 'package:brr/view/main_page/driver_main_page_view.dart';
import 'package:brr/view/mypage_page/mydata_page_view.dart';
import 'package:brr/view/history_page/history_page_view.dart';
import 'package:brr/view/loading_page/match_loading_page_view.dart';
import 'package:brr/view/location_write_page/location_write_page_view.dart';

class MainRouter {
  static final List<GetPage> routes = [
    GetPage(
      name: '/',
      page: () => MainLayout(
        child: MainPageView(),
      ),
    ),
    GetPage(
      name: '/matchlist',
      page: () => const MainLayout(
        child: MatchinglistPageView(),
      ),
    ),
    GetPage(
      name: '/mypage',
      page: () => const MainLayout(
        child: MypagePageView(),
      ),
    ),
    GetPage(
      name: '/schedule',
      page: () => const MainLayout(
        child: SchedulePageView(),
      ),
    ),
    GetPage(
      name: '/matching',
      page: () => const MainLayout(
        child: MatchingPageView(),
      ),
    ),
    GetPage(
      name: '/login',
      page: () => const LoginPageView(),
    ),
    GetPage(
      name: '/signup',
      page: () => const SignUpPageView(),
    ),
    GetPage(name: '/drivermain', page: () => MainLayout(child: DriverMainPageView())),
    GetPage(
      name: '/mydata',
      page: () => const MainLayout(
        child: MyDataPageView(),
      ),
    ),
    GetPage(
      name: '/history',
      page: () => const MainLayout(
        child: HistoryPageView(),
      ),
    ),
    GetPage(
      name: '/matchloading',
      page: () => const MainLayout(
        child: MatchLoadingPageView(),
      ),
    ),
    GetPage(
      name: '/writelocation',
      page: () => MainLayout(
        child: WriteLocationPageView(),
      ),
    ),
  ];
}
