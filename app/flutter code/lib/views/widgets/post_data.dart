import 'package:app/controllers/post_controller.dart';
import 'package:app/models/post_model.dart';
import 'package:app/views/post_details.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';

class PostData extends StatefulWidget {
  const PostData({
    super.key,
    required this.post,
  });

  final PostModel post;

  @override
  State<PostData> createState() => _PostDataState();
}

class _PostDataState extends State<PostData> {
  final PostController _postController = Get.put(PostController());
  Color likedPost = Colors.greenAccent;

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    // ignore: unused_local_variable
    var deviceHeight = MediaQuery.of(context).size.height;
    return Container(
      margin: const EdgeInsets.only(
        bottom: 10,
      ),
      padding: EdgeInsets.all(10),
      width: double.infinity,
      decoration: BoxDecoration(
        color: Color.fromARGB(255, 228, 255, 227),
        borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(10),
            topRight: Radius.circular(10),
            bottomLeft: Radius.circular(10),
            bottomRight: Radius.circular(10)),
        boxShadow: [
          BoxShadow(
            color: const Color.fromARGB(255, 85, 85, 85).withOpacity(0.3),
            spreadRadius: 1,
            blurRadius: 5,
            offset: Offset(0, 3), // changes position of shadow
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            widget.post.user!.name!,
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.w700,
              fontSize: deviceWidth * 0.047,
            ),
          ),
          Text(
            widget.post.user!.email!,
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.w400,
              fontSize: deviceWidth * 0.037,
            ),
          ),
          const SizedBox(
            height: 10,
          ),
          Text(
            widget.post.content!,
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.w500,
              fontSize: deviceWidth * 0.04,
            ),
          ),
          Row(
            children: [
              IconButton(
                onPressed: () async {
                  await _postController.likeAndDislike(widget.post.id);
                  _postController.getAllPosts();
                },
                icon: Icon(
                  Icons.thumb_up_alt_outlined,
                  color: widget.post.liked! ? Colors.green : Colors.black,
                ),
              ),
              IconButton(
                onPressed: () {
                  Get.to(() => PostDetails(
                        post: widget.post,
                      ));
                },
                icon: Icon(Icons.comment_outlined),
              )
            ],
          ),
        ],
      ),
    );
  }
}
