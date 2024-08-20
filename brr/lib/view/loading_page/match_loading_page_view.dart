import 'package:brr/design_materials/design_materials.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:brr/view/loading_circle/loading_circle.dart';
import 'package:brr/controller/add_match_list_controller.dart'; // AddMatchListController 가져오기

class MatchLoadingPageView extends StatelessWidget {
  const MatchLoadingPageView({super.key});

  @override
  Widget build(BuildContext context) {
    final AddMatchListController controller = Get.find<AddMatchListController>();

    return Scaffold(
      body: Stack(
        children: [
          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const BouncingDots(),
                const SizedBox(height: 50),
                const Text(
                  '매칭을 시도하는 중이에요',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 8),
                Obx(() => Text(  // currentMemberStatus의 변화를 감지하여 업데이트
                  controller.currentMemberStatus.value,
                  style: const TextStyle(
                    fontSize: 16,
                    color: Colors.black,
                  ),
                )),
                const SizedBox(height: 30),
                const Text(
                  '현재 인원으로 출발하기를 원하시면\n아래의 출발해요 버튼을 눌러주세요',
                  style: TextStyle(
                    fontSize: 12,
                    color: Colors.grey,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 30),
                const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.local_taxi_outlined, color: Colors.blue, size: 50),
                    SizedBox(width: 8),
                    Icon(Icons.people_outline_outlined, color: Colors.blue, size: 50),
                  ],
                ),
                const SizedBox(height: 50),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 100,
                      height: 50,
                      decoration: BoxDecoration(
                        color: Colors.blue,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.blue,
                          elevation: 0,
                          padding: EdgeInsets.zero,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                        onPressed: () {
                          // 출발 버튼 클릭 시 행동 정의
                        },
                        child: const Text(
                          '출발해요!',
                          style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 20),
                    Container(
                      width: 100,
                      height: 50,
                      decoration: BoxDecoration(
                        color: Colors.grey[300],
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.grey[300],
                          elevation: 0,
                          padding: EdgeInsets.zero,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                        onPressed: () {
                          controller.leaveLobby(); // 매칭 취소 시 WebSocket 연결 해제
                        },
                        child: const Text(
                          '매칭 취소',
                          style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: Colors.black,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          Positioned(top: 50.0, left: 30.0, child: gobackButton())
        ],
      ),
    );
  }
}
