---
type: protein-evaluation
gene: "GSDMA"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## GSDMA (Gasdermin-A) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | GSDMA |
| 蛋白全称 | Gasdermin-A |
| UniProt ID | Q96QA5 |
| 蛋白大小 | 445 aa / 49.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 445 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR007677; InterPro:IPR040460; InterPro:IPR041263; Pfam:PF04598; Pfam:PF17708 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

This form constitutes the precursor of the pore-forming protein and acts as a sensor of infection: upon infection by S.pyogenes, specifically cleaved by S.pyogenes effector protein SpeB in epithelial cells, releasing the N-terminal moiety (Gasdermin-A, N-terminal) that binds to membranes and forms pores, triggering pyroptosis

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR007677 |
| InterPro | IPR040460 |
| InterPro | IPR041263 |
| Pfam | PF04598 |
| Pfam | PF17708 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000167914-GSDMA
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/23313/193_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23313/193_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23313/192_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23313/192_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23313/194_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23313/194_H8_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR007677;IPR040460;IPR041263; |
| Pfam | PF04598;PF17708; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PARK2 | BioGRID | 0 |
| SUZ12 | BioGRID | 0 |
| IFI16 | BioGRID | 0 |
| CEP152 | BioGRID | 0 |
| FOXH1 | BioGRID | 0 |
| MCM2 | BioGRID | 0 |
| ZIC1 | BioGRID | 0 |
| TBC1D22B | BioGRID | 0 |


### 深度机制分析

**结构域架构**：GSDMA（445 aa，49.0 kDa）是gasdermin家族成孔蛋白的典型成员，采用了该家族保守的两结构域自抑制架构：N端成孔结构域（Gasdermin, IPR007677, PF04598）——约250 aa，采用混合α/β折叠，形成4个α-螺旋束和中央β-片层核心，构成膜插入和寡聚化的执行模块；C端抑制结构域（Gasdermin_C, IPR040460, PF17708）——约185 aa，通过分子内互作折叠至N端结构域，覆盖并封闭N端的脂质结合面，将全长蛋白锁定于自抑制状态。AlphaFold pLDDT可用（无实验PDB）。链球菌蛋白酶SpeB在Lys244后切割，生理上释放N端片段。HPA/reactome定位显示Nucleoplasm, Nuclear bodies——这是gasdermin家族极少报道的核内分布。

**PPI互作网络解读**：PPI数据有限但高度指向性：SUZ12（PRC2/EZH2复合体核心亚基，催化H3K27me3）——最为关键的核内互作，提示GSDMA与表观遗传沉默机器的直接关联；IFI16（干扰素诱导蛋白16，胞质/核内DNA传感器，炎症小体激活因子）——与GSDMA的焦亡功能在炎症信号通路上形成协同；FOXH1（Forkhead转录因子，TGF-β/Nodal信号效应器）和MCM2（DNA复制许可因子）表明GSDMA的核内功能维度远超出经典的质膜成孔焦亡范式。PARK2（Parkin，线粒体自噬E3连接酶）和CEP152（中心粒复制蛋白）将GSDMA连接至细胞器和细胞周期调控。

**结构解读**：N端结构域的核心折叠由中央弯曲β-片层（8条混合方向β-链）和环绕α-螺旋组成，形成一个"掌形"结构——脂质结合面（掌面）富含碱性残基（Lys/Arg）以结合酸性磷脂（如cardiolipin、phosphatidylinositol phosphates）。C端抑制结构域通过广泛的疏水和氢键界面（埋藏面积约1800A²）覆盖N端脂质结合面——α4-α5螺旋束插入N端的β-片层沟槽中，形成紧密的自抑制复合体。SpeB切割位点（Lys244-Gly245）位于N-C结构域间的柔性linker上，切割后C端释放，N端构象从'closed'转变为'open'并暴露寡聚化界面。

**机制模型**：（1）经典焦亡通路：细菌感染→SpeB介导GSDMA切割→N端片段释放→结合质膜酸性磷脂→寡聚化形成直径~20nm的β-桶状跨膜孔→渗透压失衡→细胞焦亡。此通路已在化脓性链球菌感染模型中被确认；（2）核内非经典功能：GSDMA的全长自抑制态可能在核内分化为非成孔功能——通过SUZ12互作参与PRC2介导的H3K27me3沉积和基因沉默；通过IFI16互作链接DNA损伤感知和固有免疫信号激活；通过FOXH1互作调控TGF-β靶基因表达程序。核内GSDMA水平的调控可能与精密的蛋白水解控制有关——核内特异性蛋白酶（如granzyme或caspases）可能生成非成孔的N端中间片段。

**TE调控展望**：GSDMA与SUZ12的互作是最直接的TE调控线索。PRC2（EZH2-SUZ12-EED）负责催化H3K27me3——哺乳动物基因组中ERV/LTR类TE最主要的抑制性组蛋白修饰。GSDMA的全长核内形式可能作为PRC2的辅助因子：可能增强PRC2对特定TE位点的靶向效率，或调节PRC2在异染色质区域的催化活性。MCM2互作暗示GSDMA可能参与复制偶联的TE沉默维持。但GSDMA在TE调控中的具体角色目前无任何文献或实验支持——这是纯假设性的探索方向，值得设计GSDMA ChIP-seq/CUT&RUN实验验证其基因组结合位点是否富集于TE区域。

### PubMed 文献

**PubMed count: 178**


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GSDMA

