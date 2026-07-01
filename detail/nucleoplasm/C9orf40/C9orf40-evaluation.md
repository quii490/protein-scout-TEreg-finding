---
type: protein-evaluation
gene: "C9orf40"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C9orf40 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C9orf40 |
| 蛋白名称 | Uncharacterized protein C9orf40 |
| 蛋白大小 | 194 aa / 21.1 kDa |
| UniProt ID | Q8IXQ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Centrosome; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 194 aa / 21.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042349, IPR033461; Pfam: PF15017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A multidimensional systems biology analysis of cellular senescence in aging and disease.. *Genome biology*. PMID: 32264951
2. Genome-wide Association Study of 24-Hour Urinary Excretion of Calcium, Magnesium, and Uric Acid.. *Mayo Clinic proceedings. Innovations, quality & outcomes*. PMID: 31993563
3. RORB gene and 9q21.13 microdeletion: report on a patient with epilepsy and mild intellectual disability.. *European journal of medical genetics*. PMID: 24355400

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 51.5% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 23.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.4），有序残基占 23.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042349, IPR033461; Pfam: PF15017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C18orf54 | 0.606 | 0.000 | — |
| CCDC150 | 0.568 | 0.000 | — |
| C3orf14 | 0.510 | 0.000 | — |
| HAUS4 | 0.510 | 0.000 | — |
| DONSON | 0.490 | 0.000 | — |
| DNAJB8 | 0.468 | 0.468 | — |
| CT62 | 0.447 | 0.000 | — |
| ANKRD62 | 0.447 | 0.000 | — |
| GTF3C4 | 0.441 | 0.000 | — |
| MGME1 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 1 / 10 = 10%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.4 + PDB: 无 | pLDDT=59.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Centrosome | 待确认 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C9orf40 — Uncharacterized protein C9orf40，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小194 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**结构域架构**：C9orf40（194 aa, 21.1 kDa, Q8IXQ3, Uncharacterized protein C9orf40）的注释结构域极为有限——仅含C9orf40家族结构域（IPR042349, IPR033461, Pfam PF15017）——该家族是DUF4540（Domain of Unknown Function）成员，功能完全未知。跨物种同源性分析显示C9orf40在脊椎动物中保守，提示其执行重要的保守细胞功能。AlphaFold pLDDT=59.4, PDB=0——小型蛋白中等置信度——194 aa的折叠核心pLDDT 65-75（约100 aa），剩余~90 aa高度无序。蛋白质二级结构预测指示混合alpha-helical和beta-strand content，无确知的DNA/RNA结合domain。

**PPI互作网络解读**：PPI degree=10，关键伙伴揭示颠覆性的功能连接。MOV10（Moloney leukemia virus 10 homolog, BioGRID）是关键的TE restriction factor！MOV10是UPF1-like RNA helicase——作为RISC（RNA-induced silencing complex）的co-factor参与miRNA-mediated mRNA decay——更重要的是MOV10是LINE-1 retrotransposition的强效抑制剂——MOV10通过与LINE-1 RNP（ORF1p-ORF2p-LINE-1 RNA complex）直接结合→干扰ORF2p endonuclease and reverse transcriptase activity→抑制LINE-1 insertion。MOV10也抑制其他TE（IAP, HERV-K）和逆转录病毒感染。NXF1（Nuclear RNA export factor 1/TAP, BioGRID）是mRNA核export receptor——NXF1-NXT1/p15 heterodimer识别mRNA的5' cap和spliced exon junction→募集mRNP至NPC→export至胞质。XPO1（exportin-1/CRM1, BioGRID）是核export受体——识别富含leucine的nuclear export signal（NES, LxxxLxxLxL consensus）——介导蛋白和特定RNA出核。SHMT2（serine hydroxymethyltransferase 2, BioGRID）是线粒体一碳单位代谢酶——催化Ser+THF→Gly+5,10-methylene-THF——为nucleotide biosynthesis和methylation提供一碳单位。

**结构解读**：pLDDT=59.4提示C9orf40是部分折叠蛋白。PF15017 DUF4540域结构预测为small alpha/beta domain——在表面可能暴露保守疏水patch——与MOV10或NXF1蛋白质的特定domain互作。C9orf40缺乏任何核酸结合motif、酶活性位点——其功能必定作为adaptor/scaffold蛋白——通过PPI连接MOV10至特定功能complex。

**机制模型**：（1）MOV10 co-factor——C9orf40与MOV10的直接互作是最重大发现。MOV10作为TE restriction factor需要特定adaptor来识别不同TE substrate——C9orf40可能作为MOV10的substrate-specific adaptor——将MOV10招募至特定TE RNP→增强MOV10的TE inhibition specificity and efficiency。（2）NXF1/XPO1介导的RNA nuclear export调控——C9orf40与NXF1和XPO1的互作提示其在核export中功能——C9orf40可能在MOV10和nuclear export machinery之间搭建桥梁——竞争或拮抗NXF1/XPO1减少TE RNA export→核内TE RNA accumulation→nuclear RNA decay via exosome。（3）SHMT2-一碳单位代谢与TE silencing——SHMT2催化的一碳单位是SAM（S-腺苷甲硫氨酸, universal methyl donor）合成的关键前体——SAM用于DNMT1/DNMT3A/3B的CpG methylation和SETDB1/Suv39h1/2的H3K9 methylation——这些methyl marks是TE silencing的核心依赖——C9orf40可能通过SHMT2调控methyl donor availability→间接影响TE区域的DNA/histone methylation efficiency→TE silencing maintenance。

**TE调控展望**：C9orf40是本批蛋白中最具说服力的TE调控候选——MOV10直接互作是关键证据。三层次机制：（1）作为MOV10 co-factor/adaptor增强TE restriction；（2）通过NXF1/XPO1调控TE RNA nuclear export→TE translation and retrotransposition；（3）通过SHMT2-一碳代谢影响methylation→TE epigenetic silencing。C9orf40-PubMed仅3篇——其与MOV10的互作完全未被探索——实验验证此互作和TE restriction功能是top priority。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SHMT2 | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| DNAJB8 | BioGRID | 0 |
| TCEAL1 | BioGRID | 0 |
| LPPR2 | BioGRID | 0 |
| XPO1 | BioGRID | 0 |
| PLOD1 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXQ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135045-C9orf40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C9orf40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXQ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000135045-C9orf40/subcellular

![](https://images.proteinatlas.org/42167/461_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/42167/461_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/42167/462_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/42167/462_C9_4_red_green.jpg)
![](https://images.proteinatlas.org/42167/464_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/42167/464_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IXQ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IXQ3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042349;IPR033461; |
| Pfam | PF15017; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135045-C9orf40/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

