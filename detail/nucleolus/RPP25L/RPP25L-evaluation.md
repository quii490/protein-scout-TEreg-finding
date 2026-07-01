---
type: protein-evaluation
gene: "RPP25L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## RPP25L 核蛋白评估报告
### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RPP25L |
| 蛋白全称 | Ribonuclease P protein subunit p25-like protein |
| UniProt ID | Q8N5L8 |
| 蛋白大小 | 163 aa / 17.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoli; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 163 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=1 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=87.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Alba-like_dom_sf; Alba-like_NAB; DNA/RNA-bd_Alba-like |
| PPI | 6/10 | x3 | 18.0 | PPI degree=73 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

May be a component of ribonuclease P or MRP

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR036882 | Alba-like_dom_sf |
| InterPro | IPR051958 | Alba-like_NAB |
| InterPro | IPR002775 | DNA/RNA-bd_Alba-like |
| Pfam | PF01918 | Alba |


#### 3.4 结构信息

蛋白长度 163 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164967-RPP25L

![](https://images.proteinatlas.org/52187/766_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/52187/766_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/52187/987_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/52187/987_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/52187/778_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/52187/778_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/59698/1117_E11_3_red_green.jpg)
![](https://images.proteinatlas.org/59698/1117_E11_4_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 深度机制分析

**结构域架构**: RPP25L含有一个Alba-like结构域超家族折叠（IPR036882）和DNA/RNA结合Alba-like结构域（IPR002775/PF01918）。Alba（acetylation lowers binding affinity）是一个古老的核酸结合折叠，最早发现于古菌染色质蛋白Sso10b和Ssh10b中，后来在真核生物中被招募为RNase P/MRP的附属亚基。IPR051958标注为"Alba-like_NAB"，专门将其分类为核酸结合背景下的Alba家族成员。Alba结构域的核心功能是识别双链RNA或RNA-DNA杂合体——在RNase P/MRP的语境中，这意味着RPP25L的Alba结构域可能直接结合H1 RNA（RNase P的催化RNA组分）或pre-tRNA底物。

**PPI网络解读**: RPP25L的PPI网络是五个报告中靶向性最高的。所有8个高置信度STRING互作伙伴（评分920-989）均为RNase P/MRP的蛋白亚基：RPP30（989）、POP7（989）、POP4（987）、POP5（981）、RPP38（976）、RPP40（969）、POP1（951）、RPP21（920）。这个网络毫无歧义地将RPP25L定位于RNase P和/或RNase MRP全酶复合体。RPP30是RNase P中与催化RNA H1直接互作的核心亚基，POP7/POP4/POP5构成催化核心附近的亚复合体。唯一一篇PubMed文献（PMID 35417719, Cell Rep 2022）专门研究了RPP25L与其旁系同源基因RPP25的相互作用——该研究在CRISPR-Cas9筛选框架下揭示了常染色体与性染色体编码基因间的旁系同源互作，提示RPP25L与RPP25可能存在功能冗余或组织特异性分工。

**结构诠释**: AlphaFold pLDDT=87.8为良好置信度，但ESMFold的独立折叠揭示了更细致的结构特征：平均pLDDT=0.79，仅有8.6%的残基pLDDT>0.9，而有11.7%的残基pLDDT<0.5。这种分布模式表明RPP25L是一个"折叠核心+内在无序区"的结构：163个氨基酸中，Alba结构域（约90-100个残基）形成稳定的折叠核心（βαββαββ拓扑），而N端和C端延伸区域存在显著的无序性。这种结构与RNase P附属亚基的典型特征一致——无序延伸区域提供组装柔性，允许亚基在全酶组装过程中通过诱导折叠（induced folding）适应多亚基界面。

**分子机制模型**: RPP25L是RNase P和/或RNase MRP的推定性附属亚基：(1) 在RNase P中，Alba结构域可能结合pre-tRNA的TψC臂或H1 RNA的特定茎环，辅助催化核心正确定位pre-tRNA的切割位点（5' leader与tRNA体之间的磷酸二酯键）；(2) 在RNase MRP中（核仁定位支持此功能），Alba结构域可能识别pre-rRNA ITS1区域的结构化元件，参与5.8S rRNA的成熟加工；(3) RPP25L与RPP25的旁系同源关系提示两者可能在不同组织或不同细胞周期阶段分别主导RNase P/MRP活性。C端无序区可能是翻译后修饰的热点（乙酰化、磷酸化），调控Alba结构域的核酸结合亲和力（Alba命名本身即反映乙酰化调控结合亲和力的古老机制）。

**研究/治疗意义**: RPP25L是五个候选蛋白中研究最少的（PubMed=1），这本身就是最大的研究价值。RNase P是必需酶（tRNA成熟不可或缺），但其蛋白亚基组成在不同物种间差异巨大——人类RNase P至少有10个蛋白亚基，而细菌的RNase P蛋白仅1个。RPP25L可能是灵长类或人类特异性的RNase P附属亚基，代表进化上较晚的调控层级。在癌症治疗方面，PMID 35417719的CRISPR筛选数据（Cell Rep 2022）显示RPP25L与特定癌症类型的基因依赖性相关——作为RNase P的组成部分，它可能与高增殖率肿瘤的tRNA供应需求形成合成致死关系。此外，核仁定位（HPA Approved）使其可能参与核仁应激（nucleolar stress）信号通路——核仁应激是p53激活的重要上游信号，RPP25L可作为该通路的潜在切入点。

### 4. 总体评价
★★★★  **77.0/100**  |  **nucleolus**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ribonuclease P protein subunit p25-like protein

**功能**: May be a component of ribonuclease P or MRP

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036882 |
| InterPro | IPR051958 |
| InterPro | IPR002775 |
| Pfam | PF01918 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR036882;IPR051958;IPR002775; |
| Pfam | PF01918; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPP30 | STRING | 989 |
| POP7 | STRING | 989 |
| POP4 | STRING | 987 |
| POP5 | STRING | 981 |
| RPP38 | STRING | 976 |
| RPP40 | STRING | 969 |
| POP1 | STRING | 951 |
| RPP21 | STRING | 920 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N5L8-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 1**

| 35417719 | Interrogation of cancer gene dependencies reveals paralog interactions of autosome and sex chromosome-encoded genes. | Cell Rep 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RPP25L

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/RPP25L_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.79 |
| pLDDT > 0.9 | 8.6% |
| pLDDT < 0.5 | 11.7% |
| 残基数 | 163 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

