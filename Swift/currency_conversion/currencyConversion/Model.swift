//
//  Model.swift
//  currencyConversion
//
//  Created by Saurav Dwivedi on 2023-01-21.
//

import Foundation

struct Conversion: Decodable {
    var result: Float
}

struct Symbols: Decodable {
    var symbols: Dictionary<String, String>
}

