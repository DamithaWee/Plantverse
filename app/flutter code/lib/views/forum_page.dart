import 'package:app/controllers/post_controller.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';
import 'widgets/post_field.dart';
import 'widgets/post_data.dart';

class ForumPage extends StatefulWidget {
  const ForumPage({super.key});

  @override
  State<ForumPage> createState() => _ForumPageState();
}

class _ForumPageState extends State<ForumPage> {
  final PostController _postController = Get.put(PostController());
  final TextEditingController _textController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    // ignore: unused_local_variable
    var deviceHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBar(
        title: Center(
          child: Text(
            'COMMUNITY FORUM',
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.w800,
              fontSize: deviceWidth * 0.057,
              color: const Color.fromARGB(255, 51, 51, 51),
            ),
          ),
        ),
        backgroundColor: const Color.fromARGB(255, 242, 255, 242),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              PostField(
                  hintText: 'What do you want to ask?',
                  controller: _textController),
              const SizedBox(
                height: 5,
              ),
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.greenAccent,
                    elevation: 0,
                    padding: const EdgeInsets.symmetric(
                        horizontal: 40, vertical: 10)),
                onPressed: () async {
                  await _postController.createPost(
                    content: _textController.text.trim(),
                  );
                  _textController.clear();
                  _postController.getAllPosts();
                },
                child: Obx(() {
                  return _postController.isLoading.value
                      ? const CircularProgressIndicator()
                      : Text('POST',
                          style: GoogleFonts.poppins(
                            color: Colors.black,
                            fontWeight: FontWeight.w700,
                            fontSize: deviceWidth * 0.05,
                          ));
                }),
              ),
              const SizedBox(
                height: 30,
              ),
              Text(
                'POSTS',
                style: GoogleFonts.poppins(
                  fontWeight: FontWeight.w800,
                  fontSize: deviceWidth * 0.057,
                  color: const Color.fromARGB(255, 51, 51, 51),
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              Obx(() {
                return _postController.isLoading.value
                    ? const Center(
                        child: CircularProgressIndicator(),
                      )
                    : ListView.builder(
                        shrinkWrap: true,
                        physics: const NeverScrollableScrollPhysics(),
                        itemCount: _postController.posts.value.length,
                        itemBuilder: (context, index) {
                          return PostData(
                            post: _postController.posts.value[index],
                          );
                        },
                      );
              }),
            ],
          ),
        ),
      ),
    );
  }
}
