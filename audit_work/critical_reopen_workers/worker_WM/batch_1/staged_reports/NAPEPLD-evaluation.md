---
type: protein-evaluation
gene: "NAPEPLD"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, rejected-on-reeval]
status: reevaluated
reeval_result: REJECT_CONFIRMED
original_rejection: "核定位证据弱 (Uncertain) + PubMed 183 > 100 + 胞质为主膜蛋白"
---

## NAPEPLD -- RE-EVALUATED: REJECT CONFIRMED (原始总分 71.0/180, 归一化 39.4/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAPEPLD (C7orf18) |
| 蛋白名称 | N-acyl-phosphatidylethanolamine-hydrolyzing phospholipase D |
| 蛋白大小 | 393 aa / 45.6 kDa |
| UniProt ID | Q6IQ20 |
| 核定位 (HPA IF) | Cytosol (Uncertain, 但 IF 图像可用) |
| 核定位 (UniProt) | Golgi membrane, Early endosome membrane, Nuclear envelope, Nucleoplasm |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | 核定位 Uncertain + PubMed 183 > 100 + 膜蛋白性质 |

### 2. False Rejection Recheck

**原始淘汰判定**: 核定位信号不确定 + PubMed >100 + 定位偏膜系统

**Recheck 发现**:

1. **核定位证据确实薄弱**: HPA IF 标注为 Cytosol (主要), reliability 为 Uncertain。UniProt 标注 Nuclear envelope 和 Nucleoplasm, 但这些证据来自序列分析 (ISS) 而非直接实验。整体核定位信号不令人信服。核定位得分维持 4/10。

2. **蛋白核心功能不涉及细胞核**: NAPEPLD 是膜结合磷脂酶 D, 催化 N-acyl-phosphatidylethanolamines (NAPEs) 水解生成 N-acylethanolamines (内源性大麻素前体)。其主要分布在 Golgi 膜、早期内体膜和核膜, 属于膜系统蛋白。核膜定位 (nuclear envelope) 可能仅因蛋白含有膜锚定序列, 并不代表功能性核定位。

3. **研究热度高**: PubMed strict=183 (>100), 内源性大麻素领域研究非常活跃。该蛋白作为 NAE 生物合成的关键酶, 在神经科学和代谢领域有大量文献。

4. **结构数据质量**: AlphaFold pLDDT=87.3 (良好), 4 个 PDB 全长相结构 (4QN9, 8P90, 8P96, 8PC4)。结构数据方面表现不错, 但无法弥补核定位和文献热度的问题。

**结论**: NAPEPLD 的原始淘汰理由充分且正确。这是一个典型的膜系统蛋白 (Golgi/Endosome), 虽有核膜定位但并非功能性核蛋白。核定位得分 4/10 + PubMed 183 篇 = 研究热度 0/10, 在加权体系中两项核心维度均不达标。总分 71.0/180, 建议维持 REJECT。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Cytosol (Uncertain); UniProt: Golgi/Endosome membrane + Nuclear envelope + Nucleoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 393 aa / 45.6 kDa (理想范围 200-800 aa) |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=183 篇 (>100 -> 0/10, 一票否决) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.3, pct>90=77.4%; PDB: 4QN9/8P90/8P96/8PC4 (4 个全长结构) |
| 调控结构域 | 5/10 | x2 | 10 | IPR001279 (MBL fold), IPR024884 (NAPEPLD), IPR036866; Pfam PF12706 (Lactamase_B_2) |
| PPI 网络 | 3/10 | x3 | 9 | STRING: FAAH(0.931), MGLL(0.920), PLD2(0.918) 全为 text-mining; IntAct 仅 3 互作 |
| 互证加分 | -- | max +3 | 2.0 | PDB+AF(双源) + 结构域+AF + PDB多条目 |
| **原始总分** | | | **71.0/180** | |
| **归一化总分** | | | **39.4/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol (主定位) | Uncertain |
| UniProt subcellular | Golgi apparatus membrane (ECO:0000269), Early endosome membrane (ECO:0000269), Nucleus envelope (ECO:0000269), Nucleus nucleoplasm (ECO:0000269) | Swiss-Prot |
| GO Cellular Component | Golgi apparatus (GO:0005794, IDA:UniProt); Golgi membrane (GO:0000139); early endosome (GO:0005769, ISS:UniProt); early endosome membrane (GO:0031901); nuclear envelope (GO:0005635, ISS:UniProt); nucleoplasm (GO:0005654, ISS:UniProt); cytoplasm (GO:0005737, IBA:GO_Central); extracellular exosome (GO:0070062, HDA:UniProt); neuronal cell body (GO:0043025, IBA:GO_Central); neuron projection (GO:0043005, IBA:GO_Central) | 广谱定位 |

**核定位证据分析**:
- HPA IF: Cytosol, reliability Uncertain (该定位可信度低)
- UniProt 标注 Nuclear envelope 和 Nucleoplasm, 但 evidence code 为 ISS (inferred from sequence or structural similarity), 非直接实验证据
- 蛋白主要定位在 Golgi 膜和 Endosome 膜 (IDA 级别证据)
- 核膜定位可能仅反映膜蛋白的 ER/nuclear envelope 连续性, 而非功能性核定位
- 蛋白名称中含 "phospholipase D", 提示其为膜相关酶, 这与 Golgi/endosome 定位一致

**结论**: 核定位证据薄弱, HPA Uncertain + UniProt ISS。蛋白核心功能在膜系统而非细胞核。得分 4/10 反映了核膜定位的存在但非功能性核定位。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 393 aa |
| 分子量 | 45.6 kDa |
| 理想范围 | 200-800 aa |

**评价**: 393 aa, 45.6 kDa, 处于理想范围。是实验操作友好的蛋白大小。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 183 |
| PubMed symbol_only count | 283 |
| PubMed broad count | 313 |
| 别名(未计入scoring) | C7orf18 |

**关键文献**:
1. Robledo-Montana J, Diaz-Garcia C, Martinez M et al. (2024). "Microglial morphological/inflammatory phenotypes and endocannabinoid signaling in a preclinical model of periodontitis and depression." *Journal of neuroinflammation*. PMID: 39245706
2. Minor KM, Letko A, Becker D et al. (2018). "Canine NAPEPLD-associated models of human myelin disorders." *Scientific reports*. PMID: 29643404
3. Schiano Moriello A, Allara M, Iannotti FA et al. (2025). "Deciphering the interaction between N-palmitoyl-D-glucosamine and the endocannabinoidome." *Scientific reports*. PMID: 40596256
4. Li JA, Rong Y, Mao W et al. (2022). "Gene expression profiling reveals the genomic changes caused by MLN4924 and the sensitizing effects of NAPEPLD knockdown in pancreatic cancer." *Cell cycle*. PMID: 34874801
5. Mock ED, Driever WPF, van der Stelt M et al. (2023). "Fluorescence-Based NAPE-PLD Activity Assay." *Methods in molecular biology*. PMID: 36152191

**评价**: PubMed strict=183 > 100, 研究热度维度触犯一票否决 (0/10)。内源性大麻素领域 (endocannabinoid system) 是成熟且活跃的研究领域, NAPEPLD 作为 NAE 生物合成的限速酶, 文献积累丰富。虽然部分论文来自方法学 (activity assay) 和大麻素系统泛论, 但核心功能文献数量仍然较多。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.3 |
| 高置信度残基 (pLDDT>90) 占比 | 77.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 4QN9 (X-ray 2.65A), 8P90 (X-ray 2.80A), 8P96 (X-ray 2.86A), 8PC4 (X-ray 2.85A), 均覆盖 1-393 (全长) |

**评价**: AlphaFold 预测质量良好 (mean pLDDT=87.3, 77.4% >90)。4 个 PDB 全长实验结构, 均为 X-ray 晶体学 (2.65-2.86A)。结构数据是该蛋白最突出的维度。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR001279 (Metallo-beta-lactamase superfamily), IPR024884 (NAPEPLD), IPR036866 (Ribonuclease Z/Hydroxyacylglutathione hydrolase-like) |
| Pfam | PF12706 (Lactamase_B_2) |

**染色质调控潜力分析**: NAPEPLD 属于金属-beta-内酰胺酶超家族 (MBL fold), 具有锌离子依赖的磷酸二酯酶活性。该结构域与染色质调控无已知关联。虽然 4 个 PDB 结构提供了催化机制的结构基础, 但结构域不具有转录调控或染色质修饰的已知功能。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAAH | 0.931 | 0 | 脂肪酸酰胺水解酶 |
| MGLL | 0.920 | 0 | 单酰甘油脂肪酶 |
| PLD2 | 0.918 | 0 | 磷脂酶 D2 |
| DAGLA | 0.894 | 0 | 二酰甘油脂肪酶 alpha |
| DAGLB | 0.890 | 0 | 二酰甘油脂肪酶 beta |
| GDE1 | 0.854 | 0 | 甘油磷酸二酯酶 |
| ABHD4 | 0.853 | 0 | 水解酶 |
| ABHD6 | 0.821 | 0 | 水解酶 |
| NAAA | 0.816 | 0 | N-酰基乙醇胺酸酰胺酶 |
| FAAH2 | 0.807 | 0 | 脂肪酸酰胺水解酶 2 |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DISC1 | two hybrid fragment pooling | 31413325 |
| CLEC4M | anti tag coimmunoprecipitation | 33961781 |
| (CLASH interaction partner) | clash | 23622248 |

**PPI 互证分析**:
- STRING 互作全部为 text-mining 预测 (experimental=0), 无实验验证
- IntAct 仅 3 个互作条目 (DISC1 Y2H + CLEC4M co-IP + 1 CLASH)
- PPI 网络极弱, 不支持该蛋白参与蛋白互作网络的核心节点
- STRING partners: 15, IntAct interactions: 3

**评价**: PPI 网络非常薄弱。所有 STRING 预测均来自 text-mining, 无实验 supported。IntAct 仅 3 个互作。这表明 NAPEPLD 可能以单体酶形式发挥作用, 或其主要互作对象为小分子底物 (脂质) 而非蛋白。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.3 + PDB 4 entries | pLDDT=87.3, v6, 4 PDB 全长 | 预测+实验 (高度一致) |
| 定位 | UniProt + HPA + GO | Golgi/Endosome/Nuclear envelope / Cytosol | 不一致 (HPA 说 Cytosol, UniProt 列多种膜结构) |
| PPI | STRING + IntAct | 15 (全 text-mining) + 3 interactions | 数据薄弱 |

**互证加分明细**:
- PDB + AlphaFold 双源验证 (4 全长实验结构 + 高质量预测): +0.5
- 多库定位一致: +0 (HPA=cytosol, UniProt=多种膜结构, 不一致)
- STRING + IntAct 双源验证: +0 (IntAct 仅 3 互作, 且 STRING 全 text-mining)
- 结构域 + AlphaFold 质量一致性: +0.5
- PDB 多条目覆盖 (4 entries): +1.0
**总分**: +2.0 / max +3

### 5. 总体评价

**推荐等级**: REJECT CONFIRMED (原始评估 REJECTED -> 重新评估 REJECTED)

**核心优势**:
1. 结构数据质量良好: AlphaFold pLDDT=87.3 + 4 个 PDB 全长结构
2. 蛋白大小理想 (393 aa)
3. 内源性大麻素生物合成中的关键限速酶

**劣势/不确定性**:
1. 核定位证据非常薄弱: HPA Uncertain (Cytosol), UniProt ISS (nuclear envelope)
2. PubMed 183 篇 > 100, 研究热度过高 (0/10, 加权 x5)
3. 蛋白本质是膜系统蛋白 (Golgi/Endosome membrane), 非功能性核蛋白
4. PPI 网络极弱 (全 text-mining, IntAct 仅 3 互作)
5. 核膜定位可能仅反映膜蛋白的内膜系统连续性

**False Rejection 定性**:
原始评估在核定位和研究热度两个关键维度上的判断均正确。NAPEPLD 的核定位证据薄弱 (primarily membrane system protein), PubMed 热度超过 100。核查确认其确实不适合作为 TE 调控核蛋白的候选目标。原始 REJECT 判定维持。

**下一步建议**:
- [ ] 如团队对内源性大麻素信号与 TE 调控的交集感兴趣, 可考虑研究 NAPEPLD 的上游转录调控因子, 而不是 NAPEPLD 本身
- [ ] NAPEPLD 的 4 个 PDB 结构可作为酶学研究的工具, 但不适合核蛋白筛选
- [ ] 考虑通过该蛋白的文献网络寻找下游效应蛋白 (如 FAAH, CNR1/TRPV1 等受体) 作为替代候选

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IQ20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161048-NAPEPLD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAPEPLD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IQ20
- STRING: https://string-db.org/network/9606.ENSP00000292586
- Data fetched live: 2026-06-02
