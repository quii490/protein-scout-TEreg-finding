---
type: protein-evaluation
gene: "NRL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NRL — REJECTED (研究热度过高 (PubMed strict=516，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRL / D14S46E |
| 蛋白名称 | Neural retina-specific leucine zipper protein |
| 蛋白大小 | 237 aa / 25.9 kDa |
| UniProt ID | P54845 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 237 aa / 25.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=516 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 516 |
| PubMed broad count | 9365 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: D14S46E |

**关键文献**:
1. The latex story.. *Chemical immunology and allergy*. PMID: 24925405
2. Identification and characterization of early human photoreceptor states and cell-state-specific retinoblastoma-related features.. *eLife*. PMID: 40767624
3. Mechanisms of photoreceptor protection upon targeting the Nrl-Nr2e3 pathway.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40397675
4. The latex-fruit syndrome.. *Biochemical Society transactions*. PMID: 12440950
5. Current state of occupational latex allergy.. *Current opinion in allergy and clinical immunology*. PMID: 31850921

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 31.2% |
| 低置信 (pLDDT<50) 占比 | 23.6% |
| 有序区域 (pLDDT>70) 占比 | 45.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.9，有序区 45.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008917; Pfam: PF03131, PF08383 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRX | 0.990 | 0.322 | — |
| NR2E3 | 0.954 | 0.322 | — |
| RHO | 0.889 | 0.000 | — |
| FIZ1 | 0.888 | 0.292 | — |
| FSCN2 | 0.815 | 0.000 | — |
| RPE65 | 0.798 | 0.000 | — |
| PDE6B | 0.779 | 0.000 | — |
| PDE6A | 0.743 | 0.000 | — |
| GNAT1 | 0.738 | 0.000 | — |
| RP9 | 0.738 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OPTN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23956131|imex:IM-23095 |
| EBI-9975278 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.9 + PDB: 无 | pLDDT=70.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NRL — Neural retina-specific leucine zipper protein，研究基础较多，新颖性有限。
2. 蛋白大小237 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 516 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 516 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54845
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129535-NRL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54845
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000129535-NRL/subcellular

![](https://images.proteinatlas.org/64599/1363_D8_5_red_green.jpg)
![](https://images.proteinatlas.org/64599/1363_D8_6_red_green.jpg)
![](https://images.proteinatlas.org/64599/1536_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/64599/1536_F11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P54845-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P54845 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 159..222; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR004826;IPR046347;IPR013592;IPR008917;IPR024874; |
| Pfam | PF03131;PF08383; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000129535-NRL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FIZ1 | Biogrid | false |
| OPTN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
