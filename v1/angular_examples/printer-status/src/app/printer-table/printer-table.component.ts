import {Component, OnInit} from '@angular/core';
import {Printer, PrintersResponse} from 'src/api/models';
import {PrintersService} from '../../api/services/printers.service';

@Component({
  selector: 'app-printer-table',
  templateUrl: './printer-table.component.html',
  styleUrls: ['./printer-table.component.css']
})
export class PrinterTableComponent implements OnInit {
  printers: Printer[];

  constructor(private printersService: PrintersService) { }

  ngOnInit(): void {
    this.getPrinters();
  }

  getPrinters(): void {
    this.printersService
      .getPrinters({limit: 10, offset: 0})
      .subscribe(response => this.printers = response.printers);
  }

}
