import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentySeventhItemComponent } from './twenty-seventh-item.component';

describe('TwentySeventhItemComponent', () => {
  let component: TwentySeventhItemComponent;
  let fixture: ComponentFixture<TwentySeventhItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentySeventhItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentySeventhItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
