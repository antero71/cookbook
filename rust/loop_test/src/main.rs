fn main() {
    
    let result = loop_test();
    assert_eq!(result, 20);
    println!("result is {}",result);
    let result2 = loop_test2();
    println!("result2 is {:?}",result2);
}

fn loop_test() -> u32 {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };
    result

}

fn loop_test2() -> u32 {
    let mut counter = 0;
    let mut vector: Vec<u32> = vec![0];
    let result = loop {
        counter+=1;
        if counter % 2 == 0 {
            vector.push(counter);
        }
        if counter > 10 {
            break vector.pop().unwrap_or(0);
        }
    };
    result
}
