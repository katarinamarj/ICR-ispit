import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FifteenthItemComponent } from './fifteenth-item.component';

describe('FifteenthItemComponent', () => {
  let component: FifteenthItemComponent;
  let fixture: ComponentFixture<FifteenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FifteenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FifteenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
