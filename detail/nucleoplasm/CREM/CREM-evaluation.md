---
type: protein-evaluation
gene: "CREM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CREM — REJECTED (研究热度过高 (PubMed strict=659，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREM |
| 蛋白名称 | cAMP-responsive element modulator |
| 蛋白大小 | 345 aa / 37.0 kDa |
| UniProt ID | Q03060 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 37.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=659 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR003102, IPR001630; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ATF4-CREB1 transcription factor complex (GO:1990589)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 659 |
| PubMed broad count | 1239 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection.. *Nature*. PMID: 38987588
2. Intracranial mesenchymal tumor with FET-CREB fusion-A unifying diagnosis for the spectrum of intracranial myxoid mesenchymal tumors and angiomatoid fibrous histiocytoma-like neoplasms.. *Brain pathology (Zurich, Switzerland)*. PMID: 33141488
3. MITF Pathway-Activated Cutaneous Neoplasms.. *Advances in anatomic pathology*. PMID: 40387110
4. CREB regulates Foxp3(+)ST-2(+) T(REGS) with enhanced IL-10 production.. *Frontiers in immunology*. PMID: 40777015
5. Expanding the clinicopathologic spectrum and genomic landscape of tumors with SMARCA2/4::CREM fusions.. *The Journal of pathology*. PMID: 39344423

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 18.6% |
| 低置信 (pLDDT<50) 占比 | 51.0% |
| 有序区域 (pLDDT>70) 占比 | 30.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 30.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR003102, IPR001630; Pfam: PF00170, PF02173 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREB1 | 0.990 | 0.392 | — |
| ATF2 | 0.952 | 0.000 | — |
| FHL5 | 0.947 | 0.488 | — |
| CREB3L4 | 0.933 | 0.301 | — |
| CREB3 | 0.923 | 0.000 | — |
| BCL2 | 0.922 | 0.000 | — |
| ATF4 | 0.920 | 0.047 | — |
| CREB3L2 | 0.916 | 0.000 | — |
| CREB5 | 0.915 | 0.000 | — |
| CREB3L3 | 0.911 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SAM35 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| PIAS3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CASP8AP2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| UBE2I | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SP100 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EMP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CDC5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12143|pubmed:19013276 |
| HBT1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 无 | pLDDT=60.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CREM — cAMP-responsive element modulator，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 659 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 659 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03060
- Protein Atlas: https://www.proteinatlas.org/ENSG00000095794-CREM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03060
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000095794-CREM/subcellular

![](https://images.proteinatlas.org/18352/924_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/18352/924_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/18352/932_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/18352/932_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/18352/971_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/18352/971_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q03060-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
