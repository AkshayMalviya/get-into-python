class PromostandardInventoryController < ApplicationController
  require 'hpricot'
  include General
  include ClassMethods

 soap_service namespace: 'http://www.promostandards.org/WSDL/InventoryService/1.0.0/' 
 soap_service wsdl_style: 'document'
  
 soap_action "getFilterValues",
    :args   => {:GetFilterValuesRequest => PromostandardInventoryModule::GetFilterValuesRequest },
    :return =>  {:GetFilterValuesReply => PromostandardInventoryModule::GetFilterValuesReply },
    :to => :get_filter_values
    
  def get_filter_values
  
    ##http://tektest.promo:4009/promostandard_inventory/get_filter_values
   
  #when testing from promostandard api validator and used ngrok for local server,  we require this to establish connection and comment  applicaion_controller before_filter
#      company = Setup::Company.find_by_sql(["select schema_name, erp_schema from main.dbo.main_companies where code='tektest' "])
#      schema_name = company.first.schema_name
#      ActiveRecord::Base.connection.execute("use #{schema_name}")
  
    doc = Hpricot::XML(request.raw_post) 

    wsVersion       = parse_xml(doc/:GetFilterValuesRequest/'wsVersion')
    @productID      = parse_xml(doc/:GetFilterValuesRequest/'productID')
    id              = parse_xml(doc/:GetFilterValuesRequest/'id')
   password        = parse_xml(doc/:GetFilterValuesRequest/'password')
 
    productIDtype   = parse_xml(doc/:GetFilterValuesRequest/'productIDtype')
       
    @catalog_item_inventory_details       = [];#intialized because it being used in view,(will handle case of Exception )
    if(wsVersion == '1.2.1')
      if(Admin::User.authenticate_promostandard(id, password))
        @catalog_item_inventory_details,@text = Promostandard::InventoryCrud.get_inventory_filter_values(@productID)
     
          if(@text == 'error')
           @error_message = 'Please contact system administrator.'
          end
     else
            @text          = 'error'
            @error_message = 'Username/Password is wrong.'
      end
      
    else
      @text          = 'error'
      @error_message = 'wsVersion not found.'
    end
     
     
    respond_to do |format|
      format.xml do
        render :action => "get_filter_values", content_type: 'text/xml'
      end
    end
   # render :soap => nil
    # render :soap => {:GetFilterValuesReply => response.to_s}

  end  
 
  soap_action "getInventoryLevels",
    :args   => { :Request => PromostandardInventoryModule::GetInventoryLevelsRequest },
    :return => { :Reply => PromostandardInventoryModule::GetInventoryLevelsReply },
    :to     => "get_inventory_levels"
            
  def get_inventory_levels
    ##http://tektest.promo:4009/promostandard_inventory/get_inventory_levels
    
     #when testing from promostandard api validator and used ngrok for local server,  we require this to establish connection and comment  applicaion_controller before_filter
    #    company = Setup::Company.find_by_sql(["select schema_name, erp_schema from main.dbo.main_companies where code='tektest' "])
    #    schema_name = company.first.schema_name
    #    ActiveRecord::Base.connection.execute("use #{schema_name}")
    
                  #doc = Hpricot::XML(request.raw_post)

                  #wsVersion         =         parse_xml(doc/:Request/'wsVersion')
                  @productID        =        'ccs101' #parse_xml(doc/:Request/'productID')
                    #id              =         parse_xml(doc/:Request/'id')
                    #password        =         parse_xml(doc/:Request/'password')
 #     productIDtype   = parse_xml(doc/:Request/'productIDtype')
         
    #intialized because it being used in view,(will handle case of Exception )
   @product_inventory_hash =  Hash.new; 
    
#    if(wsVersion == '1.2.1')
#      if(Admin::User.authenticate_promostandard(id, password))
        @product_inventory_hash,@text = Promostandard::InventoryCrud.get_inventory_levels()
#        if(@text == 'error')
#          @error_message = 'Please contact system administrator.'
#        end
#      else
#          @text          = 'error'
#          @error_message = 'Username/Password is wrong.'
#      end
#    else
#      @text               = 'error'
#      @error_message      = 'wsVersion not found.'
#    end
     
    respond_to do |format|
      format.xml do
        render :action => "get_inventory_levels", content_type: 'text/xml'
      end
    end
      
  end
 
end
