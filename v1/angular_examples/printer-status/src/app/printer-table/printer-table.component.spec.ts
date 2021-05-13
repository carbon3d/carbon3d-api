import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrinterTableComponent } from './printer-table.component';

describe('PrinterTableComponent', () => {
  let component: PrinterTableComponent;
  let fixture: ComponentFixture<PrinterTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PrinterTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PrinterTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
