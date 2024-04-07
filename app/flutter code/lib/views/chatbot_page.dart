import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;
// ignore: depend_on_referenced_packages

class ChatbotPage extends StatefulWidget {
  const ChatbotPage({super.key});

  @override
  State<ChatbotPage> createState() => _ChatbotPageState();
}

class _ChatbotPageState extends State<ChatbotPage> {
  final TextEditingController _textController = TextEditingController();
  List<Map<String, dynamic>> _messages = [];
  Future<void> sendMessageToRasa(String message) async {
    try {
      final response = await http.post(
        Uri.parse('http://35.198.248.164:5005/webhooks/rest/webhook'),
        headers: <String, String>{
          'Content-Type': 'application/json',
        },
        body: jsonEncode(<String, dynamic>{
          'message': message,
        }),
      );

      if (response.statusCode == 200) {
        List<dynamic> jsonResponse = jsonDecode(response.body);
        if (jsonResponse.isNotEmpty) {
          Map<String, dynamic> messageMap = jsonResponse[0];
          setState(() {
            _messages.add({'text': message, 'sentByUser': true});
            _messages.add({'text': messageMap['text'], 'sentByUser': false});
          });
        } else {
          throw Exception('Empty response from Rasa');
        }
      } else {
        throw Exception('Failed to send message to Rasa');
      }
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    var deviceHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBar(
        title: Center(
          child: Text(
            'CHATBOT',
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.w800,
              fontSize: deviceWidth * 0.057,
              color: const Color.fromARGB(255, 51, 51, 51),
            ),
          ),
        ),
        backgroundColor: const Color.fromARGB(255, 242, 255, 242),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final message = _messages[index];
                return Row(
                  mainAxisAlignment: message['sentByUser']
                      ? MainAxisAlignment.end
                      : MainAxisAlignment.start,
                  children: [
                    Container(
                      width: message['sentByUser'] ? 100 : 300,
                      margin: const EdgeInsets.symmetric(
                          vertical: 10, horizontal: 20),
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: message['sentByUser']
                            ? Colors.greenAccent
                            : Colors.grey[300],
                        borderRadius: BorderRadius.circular(15),
                      ),
                      child: Text(
                        message['text'],
                        style: TextStyle(
                          color: message['sentByUser']
                              ? Colors.black
                              : Colors.black,
                        ),
                      ),
                    ),
                  ],
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _textController,
                    decoration: const InputDecoration(
                      hintText: 'Type a message...',
                    ),
                  ),
                ),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.lightGreen,
                    elevation: 0,
                    padding: const EdgeInsets.symmetric(
                      horizontal: 30,
                      vertical: 5,
                    ),
                  ),
                  onPressed: () async {
                    String text = _textController.text.trim();
                    if (text.isNotEmpty) {
                      await sendMessageToRasa(text);
                      _textController.clear();
                    }
                  },
                  child: Text(
                    'SEND',
                    style: GoogleFonts.poppins(
                      color: Colors.black,
                      fontWeight: FontWeight.w700,
                      letterSpacing: 2.0,
                      fontSize: deviceWidth * 0.037,
                    ),
                  ),
                ),
              ],
            ),
          ),
          SizedBox(
            height: deviceHeight * 0.02,
          )
        ],
      ),
    );
  }
}
