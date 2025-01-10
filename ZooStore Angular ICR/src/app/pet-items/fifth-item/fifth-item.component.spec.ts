import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FifthItemComponent } from './fifth-item.component';

describe('FifthItemComponent', () => {
  let component: FifthItemComponent;
  let fixture: ComponentFixture<FifthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FifthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FifthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
