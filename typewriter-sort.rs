use rand::Rng;

fn typewriter_sort(lst: &Vec<i32>) -> Vec<i32> {
    let mut length = 0;

    loop {
        length += 1;
        let mut num_count = 0;

        loop {
            let random_list: Vec<i32> = (0..length).map(|_| rand::thread_rng().gen_range(0..=num_count)).collect();
            println!("{:?}", random_list);
            num_count += 1;

            if random_list == lst.iter().copied().collect::<Vec<i32>>().sorted() {
                return random_list;
            }
        }
    }
}