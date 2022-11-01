import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;

class SekToInr {
  String time;
  String rate;

  SekToInr({
    required this.time,
    required this.rate,
  });

  Future apiCall() async {
    final res = await this.fetchApi();
    this.time = res.time;
    this.rate = res.rate;
  }

  factory SekToInr.fromJson(Map<String, dynamic> json) {
    return SekToInr(
      time:
          DateTime.fromMillisecondsSinceEpoch(json['info']['timestamp'] * 1000)
              .toString()
              .split('.')[0],
      rate: json['info']['quote'].toString(),
    );
  }

  Future<SekToInr> fetchApi() async {
    final response = await http.get(
        Uri.parse(
            'https://api.apilayer.com/currency_data/convert?to=INR&from=SEK&amount=1'),
        headers: {
          'apikey': 'lWHgvT1oGQVVxprbrVswsTroUUG2DYYj',
        });

    if (response.statusCode == 200) {
      return SekToInr.fromJson(jsonDecode(response.body));
    } else {
      var res = {
        'info': {'timestamp': 1673726523, 'quote': 'Error'}
      };
      final String resJSON = jsonEncode(res);
      return SekToInr.fromJson(jsonDecode(resJSON));
    }
  }
}
