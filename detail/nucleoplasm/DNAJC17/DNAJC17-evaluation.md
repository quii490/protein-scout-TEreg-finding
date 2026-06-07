---
type: protein-evaluation
gene: "DNAJC17"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC17 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC17 |
| 蛋白名称 | DnaJ homolog subfamily C member 17 |
| 蛋白大小 | 304 aa / 34.7 kDa |
| UniProt ID | Q9NVM6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 304 aa / 34.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.0; PDB: 2D9O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR034254, IPR036869, IPR012677, IPR052 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- spliceosomal complex (GO:0005681)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Scouring the human Hsp70 network uncovers diverse chaperone safeguards buffering TDP-43 toxicity.. *bioRxiv : the preprint server for biology*. PMID: 40654997
2. DNAJC17 is localized in nuclear speckles and interacts with splicing machinery components.. *Scientific reports*. PMID: 29773831
3. The essential chaperone DNAJC17 activates HSP70 to coordinate RNA splicing and G2-M progression.. *bioRxiv : the preprint server for biology*. PMID: 37961102
4. Genome-scale CRISPR-Cas9 knockout screening in nasopharyngeal carcinoma for radiosensitive and radioresistant genes.. *Translational oncology*. PMID: 36739730
5. High-resolution melting analysis (HRM) for mutational screening of Dnajc17 gene in patients affected by thyroid dysgenesis.. *Journal of endocrinological investigation*. PMID: 29159607

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.0 |
| 高置信度残基 (pLDDT>90) 占比 | 44.7% |
| 置信残基 (pLDDT 70-90) 占比 | 39.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 7.9% |
| 有序区域 (pLDDT>70) 占比 | 84.2% |
| 可用 PDB 条目 | 2D9O |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.0，有序区 84.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR034254, IPR036869, IPR012677, IPR052094; Pfam: PF00226, PF00076 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC5L | 0.986 | 0.981 | — |
| XAB2 | 0.733 | 0.591 | — |
| ISY1 | 0.665 | 0.626 | — |
| SYF2 | 0.664 | 0.591 | — |
| CWC15 | 0.637 | 0.619 | — |
| TFPT | 0.606 | 0.000 | — |
| SNRNP200 | 0.596 | 0.445 | — |
| CWF19L1 | 0.591 | 0.577 | — |
| C15orf62 | 0.585 | 0.000 | — |
| PPIE | 0.576 | 0.471 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.0 + PDB: 2D9O | pLDDT=83.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC17 — DnaJ homolog subfamily C member 17，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小304 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVM6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104129-DNAJC17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVM6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104129-DNAJC17/subcellular

![](https://images.proteinatlas.org/40914/475_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/40914/475_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/40914/477_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/40914/477_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/40914/479_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/40914/479_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVM6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NVM6 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 11..76; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286"; DOMAIN 178..249; /note="RRM" |
| InterPro | IPR001623;IPR034254;IPR036869;IPR012677;IPR052094;IPR035979;IPR000504; |
| Pfam | PF00226;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104129-DNAJC17/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC5L | Biogrid, Opencell, Bioplex | true |
| CRNKL1 | Biogrid, Opencell | true |
| CWC15 | Biogrid, Bioplex | true |
| CWF19L1 | Biogrid, Opencell | true |
| EFTUD2 | Intact, Biogrid, Opencell | true |
| PRPF19 | Biogrid, Opencell | true |
| SNRNP200 | Biogrid, Opencell | true |
| TFIP11 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
