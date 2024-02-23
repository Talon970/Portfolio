import 'package:first_flutter/class/item_class.dart';
import 'package:first_flutter/core/constants.dart';
import 'package:first_flutter/pages/description_page.dart';
import 'package:flutter/material.dart';

class CardWidget extends StatelessWidget {
  const CardWidget({
    super.key,
    required this.box,
  });
  final ItemClass box;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) {
              return DescriptionPage(
                box: box,
              );
            },
          ),
        );
      },
      child: Card(
        child: Container(
          padding: const EdgeInsets.all(kDouble10),
          width: double.infinity,
          child: Column(
            children: [
              const SizedBox(height: kDouble5),
              Image.asset(
                box.imagePath,
                width: 200,
                height: 200,
                fit: BoxFit.cover,
              ),
              Text(
                box.title,
                style: const TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text("This is the ${box.title} Description"),
              const SizedBox(height: kDouble10),
            ],
          ),
        ),
      ),
    );
  }
}
