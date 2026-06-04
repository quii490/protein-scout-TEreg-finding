---
type: protein-evaluation
gene: "CRTC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRTC1 — REJECTED (研究热度过高 (PubMed strict=275，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRTC1 / KIAA0616, MECT1, TORC1, WAMTP1 |
| 蛋白名称 | CREB-regulated transcription coactivator 1 |
| 蛋白大小 | 634 aa / 67.3 kDa |
| UniProt ID | Q6UUV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 634 aa / 67.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=275 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.6; PDB: 7D8H, 7D8P, 7D9V |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024786, IPR024785, IPR024784, IPR024783; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Plasma membrane, Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 275 |
| PubMed broad count | 579 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0616, MECT1, TORC1, WAMTP1 |

**关键文献**:
1. Keratinocyte autophagy enables the activation of keratinocytes and fibroblastsand facilitates wound healing.. *Autophagy*. PMID: 32866426
2. MITF Pathway-Activated Cutaneous Neoplasms.. *Advances in anatomic pathology*. PMID: 40387110
3. Glycyrrhiza glabra extract as a skin-whitening Agent: Identification of active components and CRTC1/MITF pathway-inhibition mechanism.. *Journal of ethnopharmacology*. PMID: 40350048
4. Gene fusions in superficial mesenchymal neoplasms: Emerging entities and useful diagnostic adjuncts.. *Seminars in diagnostic pathology*. PMID: 37156707
5. CRTC1 enhances PD-L1-mediated tumor immunosuppression in non-small cell lung cancer via the Notch1/Akt signaling pathway.. *Frontiers in immunology*. PMID: 40977688

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.6 |
| 高置信度残基 (pLDDT>90) 占比 | 4.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 26.7% |
| 低置信 (pLDDT<50) 占比 | 59.3% |
| 有序区域 (pLDDT>70) 占比 | 14.0% |
| 可用 PDB 条目 | 7D8H, 7D8P, 7D9V |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=51.6），有序残基占 14.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024786, IPR024785, IPR024784, IPR024783; Pfam: PF12886, PF12885, PF12884 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREB1 | 0.998 | 0.440 | — |
| CRTC3 | 0.949 | 0.000 | — |
| CRTC2 | 0.922 | 0.000 | — |
| MAML2 | 0.784 | 0.000 | — |
| PER1 | 0.758 | 0.000 | — |
| MAML3 | 0.747 | 0.000 | — |
| MAML1 | 0.725 | 0.000 | — |
| SIK2 | 0.715 | 0.092 | — |
| SPRED1 | 0.671 | 0.000 | — |
| PPARGC1A | 0.661 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11897|pubmed:17979178 |
| CREB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| MEIS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14346|pubmed:20541704 |
| Ywhae | psi-mi:"MI:0663"(confocal microscopy) | pubmed:22770221|imex:IM-17656 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| KIF13B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KCTD3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.6 + PDB: 7D8H, 7D8P, 7D9V | pLDDT=51.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear bodies, Plasma membrane, Cytosol; 额外: Nucl | 一致 |
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
1. CRTC1 — CREB-regulated transcription coactivator 1，研究基础较多，新颖性有限。
2. 蛋白大小634 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 275 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=51.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 275 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UUV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105662-CRTC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRTC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UUV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
