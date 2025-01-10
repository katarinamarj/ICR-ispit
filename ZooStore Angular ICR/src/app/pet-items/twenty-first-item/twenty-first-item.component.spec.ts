import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentyFirstItemComponent } from './twenty-first-item.component';

describe('TwentyFirstItemComponent', () => {
  let component: TwentyFirstItemComponent;
  let fixture: ComponentFixture<TwentyFirstItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentyFirstItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentyFirstItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
