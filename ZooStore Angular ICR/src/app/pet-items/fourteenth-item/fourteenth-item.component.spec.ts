import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FourteenthItemComponent } from './fourteenth-item.component';

describe('FourteenthItemComponent', () => {
  let component: FourteenthItemComponent;
  let fixture: ComponentFixture<FourteenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FourteenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FourteenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
