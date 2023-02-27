import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';
import { FormGroup, FormControl } from '@angular/forms';
import { CurrenciesSchema } from './api.service';
import { ViewChild } from '@angular/core';
import { Chart, ChartConfiguration, ChartEvent, ChartType } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';

import { default as Annotation } from 'chartjs-plugin-annotation';


@Component({
    selector: 'app-api',
    templateUrl: './api.component.html',
    styleUrls: ['./api.component.css']
})

export class ApiComponent implements OnInit {
    title = 'Currency conversion historical data';
    selectedCurrencyOne: string = "SEK";
    selectedCurrencyTwo: string = "INR";
    currenciesList = new CurrenciesSchema();
    currencies: string[] = ["SEK", "INR", "EUR"];
    range = new FormGroup({
        start: new FormControl<Date | null>(null),
        end: new FormControl<Date | null>(null),
    });
    dataPoints: DataPoint[] = [];
    dataX: string[] = [];
    dataY: number[] = [];

    constructor(private apiService: ApiService) {
        Chart.register(Annotation);
    }

    ngOnInit() {
        this.getCurrencies();
    }

    getCurrencies() {
        this.apiService.getCurrencies()
            .subscribe(data => {
                console.log(data)
                this.currenciesList.success = data.success;
                this.currenciesList.currencies = Object.keys(data.currencies);
                this.currencies = this.currenciesList.currencies;
            })

    }

    getExchangeData() {
        let startDate: Date = this.range.value.start!;
        startDate.setDate(startDate.getDate() + 1);
        let endDate: Date = this.range.value.end!;
        endDate.setDate(endDate.getDate() + 1);

        this.apiService.getExchangeData(
            this.selectedCurrencyOne,
            this.selectedCurrencyTwo,
            startDate,
            endDate
        )
            .subscribe(data => {
                console.log(data);
                let rates = data.rates;
                let dates = Object.keys(rates)
                let values: { String: Number }[] = Object.values(rates)
                for (let i = 0; i < values.length; i++) {
                    this.dataPoints.push({ x: new Date(dates[i]), y: Number(Object.values(values[i])[0]) });
                    this.dataY.push(Number(Object.values(values[i])[0]));
                    this.dataX.push(new Date(dates[i]).toLocaleString('en-us', { month: 'short', day: 'numeric', year: 'numeric' }));
                    this.lineChartData.datasets[0].data = this.dataY;
                    this.lineChartData.labels = this.dataX;
                    this.lineChartData.datasets[0].label = `${this.selectedCurrencyOne} to ${this.selectedCurrencyTwo} exchange rate historical data`
                    this.chart?.update();
                }
            });
    }

    refresh() {
        window.location.reload();
        this.chart?.update();
    }

    public lineChartData: ChartConfiguration['data'] = {
        datasets: [
            {
                data: this.dataY,
                label: 'Currency exchange historical data',
                backgroundColor: 'rgba(77,83,96,0.2)',
                borderColor: 'rgba(77,83,96,1)',
                pointBackgroundColor: 'rgba(77,83,96,1)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgba(77,83,96,1)',
                fill: 'origin',
            }
        ],
        labels: this.dataX
    };

    public lineChartOptions: ChartConfiguration['options'] = {
        responsive: true,
        maintainAspectRatio: true,
        elements: {
            line: {
                tension: 0.5
            }
        },
        scales: {
            // We use this empty structure as a placeholder for dynamic theming.
            y:
            {
                position: 'left',
            },
            y1: {
                position: 'right',
                grid: {
                    color: 'rgba(255,0,0,0.3)',
                },
                ticks: {
                    color: 'red'
                }
            }
        },

        plugins: {
            legend: { display: true },
            annotation: {
                annotations: [
                    {
                        type: 'line',
                        scaleID: 'x',
                        value: 'Time',
                        borderColor: 'orange',
                        borderWidth: 2,
                        label: {
                            display: false,
                            position: 'center',
                            color: 'orange',
                            content: 'LineAnno',
                            font: {
                                weight: 'bold'
                            }
                        }
                    },
                ],
            }
        }
    };

    public lineChartType: ChartType = 'line';

    @ViewChild(BaseChartDirective) chart?: BaseChartDirective;

    // events
    public chartClicked({ event, active }: { event?: ChartEvent, active?: {}[] }): void {
        console.log(event, active);
    }

    public chartHovered({ event, active }: { event?: ChartEvent, active?: {}[] }): void {
        console.log(event, active);
    }
}

type DataPoint = {
    x: Date;
    y: Number;
}
