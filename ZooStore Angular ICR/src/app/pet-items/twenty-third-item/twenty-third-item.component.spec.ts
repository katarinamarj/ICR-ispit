import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentyThirdItemComponent } from './twenty-third-item.component';

describe('TwentyThirdItemComponent', () => {
  let component: TwentyThirdItemComponent;
  let fixture: ComponentFixture<TwentyThirdItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentyThirdItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentyThirdItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
