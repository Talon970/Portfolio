import 'package:first_flutter/core/constants.dart';
import 'package:first_flutter/core/notifires.dart';
import 'package:flutter/material.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Profile"),
      ),
      body: const Column(
        children: [
          CircleAvatar(
            backgroundImage: AssetImage("images/bild1.jpg"),
            radius: 60,
          ),
          SizedBox(
            height: kDouble20,
          ),
          ListTile(
            leading: Icon(Icons.person),
            title: Text("Flutter Mapp"),
          ),
          ListTile(
            leading: Icon(Icons.email),
            title: Text("info@fluttermapp.com"),
          ),
          ListTile(
            leading: Icon(Icons.web),
            title: Text("FlutterMapp.com"),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          isDarkModeNotifire.value = !isDarkModeNotifire.value;
        },
        child: ValueListenableBuilder(
          valueListenable: isDarkModeNotifire,
          builder: (context, isDark, child) {
            if (!isDark) {
              return const Icon(Icons.dark_mode);
            
            } else {
              return const Icon(Icons.light_mode);
            }
          },
        ),
      ),
    );
  }
}
