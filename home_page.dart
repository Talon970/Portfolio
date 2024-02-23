import 'package:first_flutter/class/item_class.dart';
import 'package:first_flutter/widget/card_widget.dart';
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Home Page"),
        backgroundColor: Colors
            .blue, // Diese Zeile explizit setzen, wenn ein spezifischer Blauton gewünscht ist.
      ),
      body:  SingleChildScrollView(
        child: Column(
          children: [
            CardWidget(
              box: ItemClass(title: "Rocket", imagePath: "images/bild1.jpg"),
            ),
            Row(
              children: [
                Expanded(
                  child: CardWidget(
              box: ItemClass(title: "Life", imagePath: "images/bild2.jpg"),
            ),
                ),
                Expanded(
                  child: CardWidget(
              box: ItemClass(title: "Earth", imagePath: "images/bild3.jpg"),
            ),
                ),
              ],
            ),
            CardWidget(
              box: ItemClass(title: "Bottom", imagePath: "images/bild4.jpg"),
            ),
          ],
        ),
      ),
      // Der Rest Ihres HomePage-Layouts...
    );
  }
}
