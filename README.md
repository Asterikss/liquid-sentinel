# liquid-sentinel

PDFs are collected using a WebScraper
->
They are sent to BankData directory
->
pdf_iter script iterates through the collected data, processes it and shortens it in case it's too long,
after identifing potential location of the interest rate
->
Then the processed data is saved in the appropriate location (parsed_data) depending on the bank and the
offer type
->
That data is then used to query an LLM, asking for the gist of it and the date that the offer is valid from and
the intrest rate to be given on the last line in the following format: "Date; interest rate". They are saved in
llm_parsed_data directory
->
feed_db script then uses those gists, collects and process the data, so that is is ready to be incorporated
into a database. The data, especially dates should be easily parsable and queryable.
->
That date is then written to json_data folder
->
From there it is incorporated into ...

