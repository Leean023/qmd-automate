import pytest
from pages.leave_credit_landing import EditLink
from utils.config import COLOR_GREEN
from utils.config import COLOR_RESET
import time


@pytest.mark.usefixtures("browser")
def test_data_availablity(browser):
    edit_link = EditLink(browser)
        
    # Fetch the table data outside the loop

    #pagination 1
    table_data = edit_link.dataAvailability()
    
    rows = edit_link.searchOrder()  
    
    for index, _ in enumerate(rows, start=1): 
       
        cells = table_data[index - 1]  
        
        for cell_index, cell in enumerate(cells, start=1):
            cell_text = cell.text.strip()
            assert cell_text != ", .", f"Row {index}, Cell {cell_index} of pagination 1: Empty data found in cell: {cell_text}"
            print(cell_text)

            
            if cell_text == ", ." and cell_text == "" :
                print(f"Row {index}, Cell {cell_index} of pagination 1: Missing or empty data found in cell of page 1:", cell.text)

    
    
    #pagination 2
    if edit_link.pagination_2nd():
        table_data2 = edit_link.dataAvailability()
        
        rows2 = edit_link.searchOrder()  
        
        for index2, _ in enumerate(rows2, start=1): 
        
            cells2 = table_data2[index2 -1]  
            
            for cell_index2, cell2 in enumerate(cells2, start=41):
                cell_text2 = cell2.text.strip()
                assert cell_text2 != ", .", f"Row {index2}, Cell {cell_index2} of pagination 1: Empty data found in cell: {cell_text2}"
                print(cell_text2)

                
                if cell_text2 == ", ." and cell_text2 == "" :
                    print(f"Row {index2}, Cell {cell_index2} of pagination 1: Missing or empty data found in cell of page 1:", cell2.text)


@pytest.mark.usefixtures("browser")
def test_text_presence(browser):
    edit_link = EditLink(browser)
    edit_link.searchField("Aljim")


@pytest.mark.usefixtures("browser")
def test_search_result(browser):
    edit_link = EditLink(browser)
    text1 = edit_link.searchResult()

    expectedResult = "Dungca, Aljim Carillo. Web Team Probationary Software Engineer Edit"

    assert text1 == expectedResult, "search result not matched for whole table row"
    print(COLOR_GREEN + "\n" + text1 + ": Passed" + COLOR_RESET)

@pytest.mark.usefixtures("browser")
def test_result_order(browser):
    edit_link = EditLink(browser)
    resultOrder = edit_link.searchOrder()

    ExpectedText = "Dungca, Aljim Carillo. Web Team Probationary Software Engineer Edit"
    for index, row in enumerate(resultOrder, start=1):
     row_text = row.text

     if ExpectedText in row_text:
        assert index == 1, 'text not found'
        print( COLOR_GREEN + f"'{ExpectedText}' found in Row {index}" + COLOR_RESET)
        break

@pytest.mark.usefixtures("browser")
def test_result_order_isAscending(browser):
    edit_link = EditLink(browser)
    
    edit_link.emptySearchField()

    edit_link.click_descending_name()
    
    #first pagination 
    first = edit_link.get_first_column_data()
    first_letters = [line.strip()[0].lower()for line in first]
    time.sleep(2)
    
    #2nd pagination
    if edit_link.pagination_2nd():
        second = edit_link.get_first_column_data()
        first_letters2nd = [line.strip()[0].lower()for line in second]
        
    #3rd pagination
    if edit_link.pagination_3rd():
        third = edit_link.get_first_column_data()
        first_letters3rd = [line.strip()[0].lower()for line in third]
       

    #4th pagination
    if edit_link.pagination_4th():
        fourth = edit_link.get_first_column_data()
        first_letters4th = [line.strip()[0].lower()for line in fourth]
       

     #5th pagination
    if edit_link.pagination_5th():
        fifth = edit_link.get_first_column_data()
        first_letters5th = [line.strip()[0].lower()for line in fifth]
       


    final_sorted = sorted(first_letters + first_letters2nd + first_letters3rd + first_letters4th + first_letters5th)
    
    sorted_data = first_letters + first_letters2nd + first_letters3rd + first_letters4th + first_letters5th 

    print(sorted_data)

    assert final_sorted == sorted_data, 'Given datas are not in ascending order'

    if (final_sorted == sorted_data):
        print(COLOR_GREEN + "Names are stored in ascending order: Passed" + COLOR_RESET)

    edit_link.reset_page_number()


@pytest.mark.usefixtures("browser")
def test_result_order_isDescending(browser):
    edit_link = EditLink(browser)

    edit_link.click_descending_name()
    
    edit_link.emptySearchField()

   
    
    #first pagination 
    first = edit_link.get_first_column_data()
    first_letters = [line.strip()[0].lower()for line in first]
    time.sleep(2)
    
    #2nd pagination
    if edit_link.pagination_2nd():
        second = edit_link.get_first_column_data()
        first_letters2nd = [line.strip()[0].lower()for line in second]
        

    #3rd pagination
    if edit_link.pagination_3rd():
        third = edit_link.get_first_column_data()
        first_letters3rd = [line.strip()[0].lower()for line in third]
      

    #4th pagination
    if edit_link.pagination_4th():
        fourth = edit_link.get_first_column_data()
        first_letters4th = [line.strip()[0].lower()for line in fourth]
        

     #5th pagination
    if edit_link.pagination_5th():
        fifth = edit_link.get_first_column_data()
        first_letters5th = [line.strip()[0].lower()for line in fifth]
        
    
    sorted_data = first_letters + first_letters2nd + first_letters3rd + first_letters4th + first_letters5th
    

    assert sorted_data[0].startswith("z") and sorted_data[-1].endswith("a"), 'Names are not in descending order'

    if (sorted_data[0].startswith("z") and sorted_data[-1].endswith("a")):
        print(COLOR_GREEN + "Names are stored in descending order: Passed" + COLOR_RESET)



@pytest.mark.usefixtures("browser")
def test_invalid_search_input(browser):
    edit_link = EditLink(browser)
    edit_link.searchField("hjdshdjh")

    empty_text = edit_link.empty_result()

    print(COLOR_GREEN + "Empty result indicator found: Passed" + COLOR_RESET)
    edit_link.emptySearchField()

    assert empty_text == "No matching records found", "No empty result indicator found"
    


