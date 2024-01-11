use std::str::CharIndices;

fn c2u(c: char) -> Option<u8> {
    return match c {
        '0' => Some(0),
        '1' => Some(1),
        '2' => Some(2),
        '3' => Some(3),
        '4' => Some(4),
        '5' => Some(5),
        '6' => Some(6),
        '7' => Some(7),
        '8' => Some(8),
        '9' => Some(9),
        _ => None,
    };
}

fn simple(line: &str) -> u8 {
    let i: &mut u8;
    let d1: &mut u8;
    for idx_char in line.char_indices() {
        if let Some(d1) = c2u(idx_char.1) {
            i = From::<u8>.from(idx_char.0);
            break;
        }
    }
    let j: &mut u8 = line.len() - 1;
}

// fn t1(s: &str) -> u32 {
//     s.lines().map(|line| line.into_iter().map(|c| c.into()))
// }

#[test]
fn test_simple() {
    assert_eq!(12, simple("1abc2"));
    assert_eq!(38, simple("pqr3stu8vwx"));
    assert_eq!(15, simple("a1b2c3d4e5f"));
    assert_eq!(77, simple("treb7uchet"))
}

// #[test]
// fn test_t1() {
//     let eg = "1abc2
// pqr3stu8vwx
// a1b2c3d4e5f
// treb7uchet";
//     assert_eq!(142, t1(eg));
// }
