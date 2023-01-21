//
//  Network.swift
//  currencyConversion
//
//  Created by Saurav Dwivedi on 2023-01-20.
//

import SwiftUI

class Network: ObservableObject {
    @Published var symbols: Symbols = Symbols(symbols: ["SEK": "Swedish Kroner"])
    @Published var response: Conversion = Conversion(result: 0.0)
    @Published var symbolsShort: [String] = ["SEK", "TEST"]
    

    func getExchangeRate() {
        // let urlSymbols = "https://api.apilayer.com/exchangerates_data/symbols"
        let urlExchange = "https://api.apilayer.com/exchangerates_data/convert?to=INR&from=SEK&amount=1"
        guard let url = URL(string: urlExchange) else { fatalError("Missing URL") }

        var urlRequest = URLRequest(url: url)
        urlRequest.addValue("mPeEQPVuAtxVR2LFYXAlRclZtbGApyOh", forHTTPHeaderField: "apikey")

        let dataTask = URLSession.shared.dataTask(with: urlRequest) { (data, response, error) in
            if let error = error {
                print("Request error: ", error)
                return
            }

            guard let response = response as? HTTPURLResponse else { return }

            if response.statusCode == 200 {
                guard let data = data else { return }
                DispatchQueue.main.async {
                    do {
                        // let decodedDict = try JSONDecoder().decode(Symbols.self, from: data)
                        // self.symbols = decodedDict
                        // self.symbolsShort = [String](decodedDict.symbols.keys)
                        let decodedDictRes = try JSONDecoder().decode(Conversion.self, from: data)
                        self.response = decodedDictRes
                        print(self.response)
                    } catch let error {
                        print("Error decoding: ", error)
                    }
                }
            } else {
                print("Status code \(response.statusCode). An error ocurred in API call")
            }
        }

        dataTask.resume()
    }
}
