---
type: protein-evaluation
gene: "BAG3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BAG3 — REJECTED (研究热度过高 (PubMed strict=703，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BAG3 / BIS |
| 蛋白名称 | BAG family molecular chaperone regulator 3 |
| 蛋白大小 | 575 aa / 61.6 kDa |
| UniProt ID | O95817 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Basal body; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 575 aa / 61.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=703 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039773, IPR036533, IPR003103, IPR001202, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Basal body | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- aggresome (GO:0016235)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 703 |
| PubMed broad count | 953 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BIS |

**关键文献**:
1. An astrocyte BMAL1-BAG3 axis protects against alpha-synuclein and tau pathology.. *Neuron*. PMID: 37315555
2. The chaperone-assisted selective autophagy complex dynamics and dysfunctions.. *Autophagy*. PMID: 36594740
3. BAG3 Overexpression Attenuates Ischemic Stroke Injury by Activating Autophagy and Inhibiting Apoptosis.. *Stroke*. PMID: 37377010
4. Genome-wide association and Mendelian randomisation analysis provide insights into the pathogenesis of heart failure.. *Nature communications*. PMID: 31919418
5. Cardiac fibroblast BAG3 regulates TGFBR2 signaling and fibrosis in dilated cardiomyopathy.. *The Journal of clinical investigation*. PMID: 39744939

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 18.3% |
| 低置信 (pLDDT<50) 占比 | 57.6% |
| 有序区域 (pLDDT>70) 占比 | 24.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 24.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039773, IPR036533, IPR003103, IPR001202, IPR036020; Pfam: PF02179, PF00397 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPB8 | 0.999 | 0.841 | — |
| HSPA8 | 0.999 | 0.867 | — |
| HSPA4 | 0.999 | 0.875 | — |
| STUB1 | 0.999 | 0.775 | — |
| BCL2 | 0.986 | 0.301 | — |
| HSPA1B | 0.983 | 0.875 | — |
| HSPB1 | 0.980 | 0.785 | — |
| BAG2 | 0.977 | 0.292 | — |
| BAG1 | 0.967 | 0.226 | — |
| HSP90AB1 | 0.960 | 0.385 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPB8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EBI-747182 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HSP70-1 | psi-mi:"MI:0047"(far western blotting) | pubmed:16003391|imex:IM-18904 |
| AMOT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| WIPI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Irak1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| IRAK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 无 | pLDDT=57.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol; 额外: Nucleoplasm, Basal body | 一致 |
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
1. BAG3 — BAG family molecular chaperone regulator 3，研究基础较多，新颖性有限。
2. 蛋白大小575 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 703 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 703 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95817
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151929-BAG3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BAG3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95817
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
