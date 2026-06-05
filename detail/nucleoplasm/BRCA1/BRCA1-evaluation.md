---
type: protein-evaluation
gene: "BRCA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BRCA1 — REJECTED (研究热度过高 (PubMed strict=11526，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRCA1 / RNF53 |
| 蛋白名称 | Breast cancer type 1 susceptibility protein |
| 蛋白大小 | 1863 aa / 207.7 kDa |
| UniProt ID | P38398 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Nucleus; Chromosome; Cytoplasm; Cytoplasm; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1863 aa / 207.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=11526 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=41.6; PDB: 1JM7, 1JNX, 1N5O, 1OQA, 1T15, 1T29, 1T2U |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011364, IPR031099, IPR025994, IPR001357, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome; Cytoplasm; Cytoplasm; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- BRCA1-A complex (GO:0070531)
- BRCA1-B complex (GO:0070532)
- BRCA1-BARD1 complex (GO:0031436)
- BRCA1-C complex (GO:0070533)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- DNA repair complex (GO:1990391)
- gamma-tubulin ring complex (GO:0000931)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11526 |
| PubMed broad count | 25570 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF53 |

**关键文献**:
1. BRCA1 as target for breast cancer prevention and therapy.. *Anti-cancer agents in medicinal chemistry*. PMID: 25329591
2. A strong candidate for the breast and ovarian cancer susceptibility gene BRCA1.. *Science (New York, N.Y.)*. PMID: 7545954
3. Breast cancer risks associated with missense variants in breast cancer susceptibility genes.. *Genome medicine*. PMID: 35585550
4. BRCA1 Antibodies Matter.. *International journal of biological sciences*. PMID: 34421362
5. BRCA1 gene: function and deficiency.. *International journal of clinical oncology*. PMID: 28884397

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 41.6 |
| 高置信度残基 (pLDDT>90) 占比 | 11.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 80.4% |
| 有序区域 (pLDDT>70) 占比 | 17.4% |
| 可用 PDB 条目 | 1JM7, 1JNX, 1N5O, 1OQA, 1T15, 1T29, 1T2U, 1T2V, 1Y98, 2ING |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=41.6），有序残基占 17.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011364, IPR031099, IPR025994, IPR001357, IPR036420; Pfam: PF00533, PF12820, PF00097 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MDC1 | 0.999 | 0.833 | — |
| PALB2 | 0.999 | 0.944 | — |
| BRCA2 | 0.999 | 0.896 | — |
| RAD50 | 0.999 | 0.994 | — |
| BARD1 | 0.999 | 0.999 | — |
| TP53 | 0.999 | 0.895 | — |
| MRE11 | 0.999 | 0.994 | — |
| ABRAXAS1 | 0.999 | 0.994 | — |
| FANCD2 | 0.999 | 0.779 | — |
| H2AX | 0.999 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| brca1.L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11990|pubmed:17081976 |
| bard1.L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11990|pubmed:17081976 |
| RHAMM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11990|pubmed:17081976 |
| numa1.S | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11990|pubmed:17081976 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| ZNF350 | psi-mi:"MI:0018"(two hybrid) | pubmed:11090615 |
| BRAP | psi-mi:"MI:0018"(two hybrid) | pubmed:9497340|mint:MINT-65476 |
| KPNA2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9497340|mint:MINT-65476 |
| ESR1 | psi-mi:"MI:0096"(pull down) | pubmed:15674350|imex:IM-19371 |
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=41.6 + PDB: 1JM7, 1JNX, 1N5O, 1OQA, 1T15,  | pLDDT=41.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm; Cytoplasm; Cytopla / Nuclear bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BRCA1 — Breast cancer type 1 susceptibility protein，研究基础较多，新颖性有限。
2. 蛋白大小1863 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 11526 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=41.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 11526 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P38398
- Protein Atlas: https://www.proteinatlas.org/ENSG00000012048-BRCA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRCA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P38398
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P38398-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000012048-BRCA1/subcellular

![](https://images.proteinatlas.org/4840/1852_D3_20_cr5afd37edbb5e8_red_green.jpg)
![](https://images.proteinatlas.org/4840/1852_D3_29_cr5afd37edbb5e9_red_green.jpg)
![](https://images.proteinatlas.org/4840/1913_F13_1_red_green.jpg)
![](https://images.proteinatlas.org/4840/1913_F13_2_red_green.jpg)
![](https://images.proteinatlas.org/4840/1914_E5_15_cr5c8770e98e94d_red_green.jpg)
![](https://images.proteinatlas.org/4840/1914_E5_29_cr5c8770e98ed84_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
