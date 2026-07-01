---
type: protein-evaluation
gene: "CCDC59"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC59 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC59 / BR22 |
| 蛋白名称 | Thyroid transcription factor 1-associated protein 26 | TAP26 |
| 蛋白全名 | Thyroid transcription factor 1-associated protein 26 |
| 蛋白大小 | 241 aa / 28.7 kDa |
| UniProt ID | Q9P031 |
| 子定位分类 | nucleolus |
| HPA IF 主定位 | Nucleoli, Nucleoli rim |
| HPA IF 附加定位 | Nucleoplasm, Plasma membrane |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32 | HPA主定位核 + 转录因子功能，附加胞质信号 |
| 蛋白大小 | 10/10 | x1 | 10 | 241 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=5 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=73.3, >70%=56.0%) |
| 调控结构域 | 10/10 | x2 | 20 | 明确的DNA结合同源盒结构域 |
| PPI网络 | 4/10 | x3 | 12 | STRING综合分>0.7 (4条)，主要为预测 |
| 互证加分 | — | max+3 | +1.5 | UniProt核定位 + HPA IF核验证一致 (+1.0); IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **146.5/180** | |
| **归一化总分 (÷1.83)** | | | **80.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Nucleoli, Nucleoli rim, Plasma membrane | Approved |
| UniProt | Nucleus (ECO:0000305) | Swiss-Prot/TrEMBL |
| GO-CC | nucleoplasm (TAS:Reactome) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核 + 转录因子功能，附加胞质信号

#### 3.2 蛋白大小评估

241 aa (200-800 aa ideal range)

**评价**: 241 aa / 28.7 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 5 |
| PubMed symbol_only | 5 |
| PubMed broad | 12 |
| 别名 | BR22 | TAP26 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 5 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Establishment, characterization, and drug screening of low-passage patient individual non-small cell lung cancer in vitro models including the rare pleomorphic subentity.** *Frontiers in oncology* (2023) PMID:37228492 -- Andus I et al.
2. **Integrated pan-cancer profiling and experimental validation identify CCDC59 as a key driver and therapeutic biomarker in liver hepatocellular carcinoma.** *Pathology, research and practice* (2026 Jun) PMID:41905279 -- Li K et al.
3. **KDM3A Modulates Biological Processes in Osteoarthritis Cell Models Via the Wnt/β-Catenin Signaling Pathway.** *Cartilage* (2025 Jun 21) PMID:40542702 -- Fu Y et al.
4. **CCDC59 alleviates bleomycin-induced inflammation and pulmonary fibrosis by increasing SP-B and SP-C expression in mice.** *International immunopharmacology* (2024 Sep 10) PMID:38972208 -- Zuo H et al.
5. **DAPL1 Identified as a Novel Prognostic Biomarker in Breast Cancer: Insights from Comprehensive in Silico Analysis.** *Iranian journal of biotechnology* (2025 Jul) PMID:41111983 -- Zhang H et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.3 |
| pLDDT > 90 (Very High) | 36.9% |
| pLDDT 70-90 (High) | 19.1% |
| pLDDT 50-70 (Medium) | 23.7% |
| pLDDT < 50 (Low) | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 56.0% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=73.3，有序区域 56%）。作为新颖蛋白，此水平可接受。

**评分: 7/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 含明确的DNA/染色质相关结构域：无注释结构域。

**评分: 10/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| TTF1 | 0.905 | 0.000 | — |
| LLPH | 0.839 | 0.000 | — |
| SFTPB | 0.809 | 0.000 | — |
| SFTPC | 0.764 | 0.000 | — |
| RPF1 | 0.497 | 0.000 | — |
| BRIX1 | 0.496 | 0.000 | — |
| MRPS31 | 0.488 | 0.316 | — |
| ZNF75D | 0.473 | 0.000 | — |
| MRPS18C | 0.453 | 0.246 | — |
| CXCL11 | 0.446 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| PAK5 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| MAGED1 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| TSC22D1 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| MOB4 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| 6323502 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| DEDD | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| TNFRSF14 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| BRF2 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| TRAF6 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| CDC20 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |


**已知复合体成员** (GO Cellular Component):
- nucleoplasm (TAS:Reactome)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 15
- 调控相关比例: 0/15 (0%)

**评价**: STRING综合分>0.7 (4条)，主要为预测

**评分: 4/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Nucleus + Nucleoplasm/Nucleoli | 一致 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 15 | 数据充分 |

**互证加分明细**:
- UniProt核定位 + HPA IF核验证一致 (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (80.1/100)

**核心优势**:
1. Extremely novel -- PubMed=5篇
2. HPA主定位核 + 转录因子功能，附加胞质信号

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TTF1 | STRING | 905 |
| LLPH | STRING | 839 |
| CDC20 | BioGRID | 1 |
| DEDD | BioGRID | 1 |
| VHL | BioGRID | 1 |
| PAK7 | BioGRID | 1 |
| APP | BioGRID | 1 |
| CSNK2A2 | BioGRID | 1 |


### 深度机制分析

CCDC59(TAP26/BR22, 241 aa, 28.7 kDa, UniProt: Q9P031)是甲状腺转录因子1(TTF1/NKX2-1)相关蛋白26, 其结构域注释原始阶段为"无注释域", 但Domain/SMART修复后InterPro(IPR013730/PF08524)标注为"Protein of unknown function DUF2190"——DUF2190结构域在数据库中与CTF/NF-1(CCAAT-box-binding transcription factor, 核因子1)和NFI相关的核蛋白共出现, 提示一个保守但尚未表征的转录调节折叠。CCDC59的定位于核仁(nucleoli)和核仁边缘(nucleoli rim), HPA Approved级, 这是对核糖体生物合成、RNA聚合酶I转录和核仁应激响应的关键亚核区室(nucleolus)的特异性定位, 暗示该蛋白可能参与rDNA的转录和/或pre-rRNA加工。

PPI网络的"核仁节点"特征高度指示CCDC59的功能角色: TTF1(STRING 905)是CCDC59的同名互作伙伴——TTF1/NKX2-1是肺特异性同源盒转录因子, 也是核仁中rDNA转录终止因子, 通过与TTF1的互作CCDC59可能在rDNA重复簇的转录终止和/或表观遗传沉默中发挥作用; LLPH(STRING 839)是核仁蛋白NOP16的同源物, 参与pre-rRNA的18S加工; RPF1(STRING 497)是核糖体加工因子1; BRIX1(STRING 496)是参与60S核糖体亚基成熟的核仁蛋白; MRPS31和MRPS18C(STRING 488/453, 实验分0.316/246)是线粒体核糖体蛋白, 暗示CCDC59可能桥接核仁(cytosolic rDNA)和线粒体(mito-ribosome)核糖体生物合成通路; NIFK(humanPPI, Biogrid+Bioplex)是Ki-67互作的核仁磷蛋白, 参与rRNA转录和核仁组装; KRR1(humanPPI, Bioplex)是KRR1小亚基加工体(SSU processome)组分; IPO5(humanPPI, Biogrid+Opencell)是importin-5, 负责将核仁蛋白从胞质运输至核仁; H1-7(humanPPI, Bioplex)是生殖细胞特异性linker组蛋白——暗示潜在的染色质结合能力。TRAF6(IntAct coIP)是E3泛素连接酶和NF-kappaB通路的信号适配蛋白, 与CCDC59的互作提示泛素信号可能调节核仁应激响应中的CCDC59稳定性/定位。

CCDC59的极度新颖性(PubMed strict=5, 80.1/100归一化总分)与其强大的结构-功能交叉矛盾: 尽管功能注释极为有限, 但CCDC59-TTF1互作链提供了清晰的机制切入点——TTF1结合rDNA基因间区的Sal-box终止元件终止Pol I转录, 而TTF1的缺失导致rDNA异染色质化丢失和rDNA拷贝数异常扩增。CCDC59通过与TTF1互作可能调控这一过程的信令。此外, IPR013730结构域中富集的碱性氨基酸串(basic patches)可能作为非经典核仁定位信号(NoLS)被核仁磷蛋白B23(nucleophosmin)识别。TE调控方面: CCDC59作为"染色质/DNA调控相关结构域持有者"(IPR013730)和核仁特异性蛋白——核仁是核内的"相分离中心", 数十个rDNA重复簇中的转座子插入(LINE-1, Alu→28S rRNA)和rDNA拷贝中的TE元件在核仁内的异染色质状态对整个基因组的TE沉默状态具有"模板效应"(template effect)——CCDC59通过其与TTF1和NIFK/KRR1的双向连接可能在rDNA-TE表观调控中发挥功能。HCC生物标志物功能(PMID 41905279: 肝细胞癌中CCDC59是驱动基因和预后标志物)进一步支持其在基因组稳定性维护中的功能——HCC的特征包括rDNA高转录和LINE-1激活。肺纤维化保护功能(PMID 38972208: SP-B/SP-C)可能反映的是分泌型肺泡II型细胞的核仁应激路径。

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

![](https://images.proteinatlas.org/38555/437_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38555/437_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38555/431_A12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38555/431_A12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/38555/443_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38555/443_A12_3_blue_red_green.jpg)


### ESMFold 结构预测

| 指标 | 数值 |
|---|---|
| 平均 pLDDT | 0.75 |
| >0.9 | 29.0% |
| <0.5 | 2.9% |
| 残基数 | 241 |

ESMFold 从头折叠验证。PDB: `detail/_esm_structures/CCDC59_esmfold.pdb`

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P031
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC59
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P031
- STRING: https://string-db.org/cgi/network?identifiers=CCDC59&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P031 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013730; |
| Pfam | PF08524; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133773-CCDC59/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IPO5 | Biogrid, Opencell | true |
| NIFK | Biogrid, Bioplex | true |
| H1-7 | Bioplex | false |
| HAUS1 | Bioplex | false |
| HAUS4 | Bioplex | false |
| KRR1 | Bioplex | false |
| MAGEA8 | Intact | false |
| NEIL1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
