import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentySecondItemComponent } from './twenty-second-item.component';

describe('TwentySecondItemComponent', () => {
  let component: TwentySecondItemComponent;
  let fixture: ComponentFixture<TwentySecondItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentySecondItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentySecondItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
