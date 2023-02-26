import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {

    baseURL: string = "https://api.apilayer.com/";

    constructor(private http: HttpClient) {
    }

    getCurrencies(): Observable<CurrenciesSchema> {
        console.log('getCurrencies ' + this.baseURL)
        const headers = { 'apikey': 'lWHgvT1oGQVVxprbrVswsTroUUG2DYYj' }
        return this.http.get<CurrenciesSchema>(this.baseURL + "currency_data/list", { 'headers': headers })
    }

    getExchangeData(
        selectedCurrencyOne: string,
        selectedCurrencyTwo: string,
        rangeStart: Date,
        rangeEnd: Date): Observable<ExchangeSchema> {
        const headers = { 'apikey': 'lWHgvT1oGQVVxprbrVswsTroUUG2DYYj' }
        return this.http.get<ExchangeSchema>(
            this.baseURL + `exchangerates_data/timeseries?start_date=${rangeStart.toISOString().split('T')[0]}&end_date=${rangeEnd.toISOString().split('T')[0]}&base=${selectedCurrencyOne}&symbols=${selectedCurrencyTwo}`,
            { 'headers': headers }
        )
    }

}

export class CurrenciesSchema {
    success: boolean
    currencies: string[]
}

class ExchangeSchema {
    success: boolean
    rates: { String: { String: Number } }
}