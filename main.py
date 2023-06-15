import time
import link_class


def main():
    # start_url = 'https://en.wikipedia.org/wiki/Six_degrees_of_separation'
    # target_url = 'https://en.wikipedia.org/wiki/Disney_Entertainment'
    # start_url = 'https://en.wikipedia.org/wiki/Russia '
    # target_url = 'https://en.wikipedia.org/wiki/China'
    start_url = 'https://en.wikipedia.org/wiki/Yuri_Gagarin'
    target_url = 'https://en.wikipedia.org/wiki/Yang_Liwei'
    #https://en.wikipedia.org/wiki/Russia  https://en.wikipedia.org/wiki/China   https://en.wikipedia.org/wiki/Yang_Liwei
    root_url = 'https://en.wikipedia.org'
    rate_limit = 5
    start_time = time.time()

    link_finder1 = link_class.WikiLinkFinder(start_url, target_url, rate_limit,root_url,start_time)
    result1 = link_finder1.find_link_chain()
    link_finder2 = link_class.WikiLinkFinder(target_url,start_url, rate_limit,root_url,start_time)
    result2 = link_finder2.find_link_chain()

    if result1:
        print(f'Link chain found: {" => ".join(result1)}')
    else:
        print('No link chain found within the limit1.')
    if result2:
        print(f'Link chain found: {" => ".join(result2)}')
    else:
        print('No link chain found within the limit2.')


if __name__ == '__main__':
    main()



